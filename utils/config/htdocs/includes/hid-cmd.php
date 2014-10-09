<?php 
	$lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
	switch ($lang){
   	 	case "fr":
			$lang="fr_FR";
        		break;
		default:
			$lang="C";
			break;
	}
	if (isset($_POST['action']) && $_POST['action'] === 'updateSource' && isset($_POST['tab']) && $_POST['tab'] == 'cmd'):
		$new_source = trim(strip_tags($_POST['source']));
		file_put_contents($files['hid-cmd']['path'], $new_source);	
		$message = 'Source updated!';
	elseif (isset($_GET['action']) && $_GET['action'] === 'execute' && isset($_GET['tab']) && $_GET['tab'] == 'cmd'):
		$elevated = isset($_GET['elevated']) && (int) $_GET['elevated'] === 1	?	1	:0;
		$platform = isset($_GET['platform']) && in_array(strip_tags(trim($_GET['platform'])), array('windows7', 'windows8'))	?		strip_tags(trim($_GET['platform']))	:	'';
		if ($elevated === 0) {
			$res = shell_exec("LANG=$lang start-hid-cmd");
			$message = 'Attack executed!';
		}
		elseif (!empty($platform)) {
			switch($platform):
			case 'windows7':
				$res = shell_exec("LANG=$lang start-hid-cmd-elevated-win7");
				break;
			case 'windows8':
				$res = shell_exec("LANG=$lang start-hid-cmd-elevated-win8");
				break;
				endswitch;
				$message = 'Attack executed!';
		} else {
			$message = 'Invalid options!';
		}
		ob_clean();
		echo $message;
		die();
	endif;
	$con = file_get_contents($files['hid-cmd']['path']);
?>
<?php require dirname(__FILE__).'/messages.php';?>
<ul class="nav nav-tabs" role="tablist">
	<li class="active"><a href="#cmdsource" role="tab" data-toggle="tab">Source</a></li>  				
</ul>
<div class="tab-content" id="cmd-tab">
	<div id="cmdsource" class="tab-pane fade in active">
		<form action="index.php#cmd" method="POST">
			<input type="hidden" name="k" value="hid" />
			<input type="hidden" name="tab" value="cmd" />
			<input type="hidden" name="action" value="updateSource" />
			<div class="form-group">		
				<textarea name="source" id="input-source" class="form-control panel-body md-input" rows="20"><?php echo $con;?></textarea>
			</div>
			<input class="btn btn-primary btn-sm" type="submit" value="Update" name="commit">
		</form>
	</div>
</div> <!-- end of .tab-content -->

<div class="bottom-buttons-group">
	<form action="index.php?#cmd" method="post" class="form-inline" id="cmd-elevator-form" onsubmit="return elevatorFormSubmited('cmd');">
		<input type="hidden" name="k" value="hid">
		<input type="hidden" name="tab" value="cmd">
		<input type="hidden" name="action" value="execute"> 
		<input class="btn btn-success btn-sm fixed-btn" type="submit" value="Execute" name="commit">
		<a href="javascript:void(0);" onclick="return resetUsb('cmd');" class="fixed-btn"><input class="btn btn-warning btn-sm" type="button" value="Reset USB" name="commit"></a>
		
		<label class="checkbox-inline fixed-btn" for="cmd-elevated" style="margin-top:4px;">
  			<input type="checkbox" id="cmd-elevated" name="elevated" class="hidsCheck"> Admin 
		</label>
		<select class="fixed-btn select2drop" name="platform" id="cmd-platform">
  			<option value="windows7">Win7</option>
  			<option value="windows8">Win8</option>
		</select>
	</form>
</div>
