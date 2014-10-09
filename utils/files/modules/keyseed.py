#!/usr/bin/python

# Formats payload to HID Keyboard sequences. Real rough poc for testing basic payloads.
import locale

global_last_char=""

def findinfrenchlist(byte):
	global global_last_char;
	found_matching_composed_char=False
	if ( global_last_char=="\xc3" ):
		# We have a UTF-8 char
		if byte=="\xa9":
			print '''echo -ne "\\x00\\x00\\x00\\x1f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # LATIN SMALL LETTER E WITH ACUTE
			found_matching_composed_char=True
		elif byte=="\xa8":
			print '''echo -ne "\\x00\\x00\\x00\\x24\\x00\\x00\\x00\\x00" > /dev/hidg0''' # LATIN SMALL LETTER E WITH GRAVE
			found_matching_composed_char=True
		elif byte=="\xa7":
			print '''echo -ne "\\x00\\x00\\x00\\x26\\x00\\x00\\x00\\x00" > /dev/hidg0''' # LATIN SMALL LETTER C WITH CEDILLA
			found_matching_composed_char=True
		elif byte=="\xa0":
			print '''echo -ne "\\x00\\x00\\x00\\x27\\x00\\x00\\x00\\x00" > /dev/hidg0''' # LATIN SMALL LETTER A WITH GRAVE
			found_matching_composed_char=True
		elif byte=="\xb9":
			print '''echo -ne "\\x00\\x00\\x00\\x34\\x00\\x00\\x00\\x00" > /dev/hidg0''' # LATIN SMALL LETTER U WITH GRAVE
			found_matching_composed_char=True
	elif ( global_last_char=="\xc2" ):
		# We have a UTF-8 char
		if byte=="\xb0":
			print '''echo -ne "\\x20\\x00\\x00\\x2d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # DEGREE SIGN
			found_matching_composed_char=True
		elif byte=="\xa8":
			print '''echo -ne "\\x20\\x00\\x00\\x2f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # DIAERESIS
			found_matching_composed_char=True
		elif byte=="\xa3":
			print '''echo -ne "\\x20\\x00\\x00\\x30\\x00\\x00\\x00\\x00" > /dev/hidg0''' # POUND SIGN
			found_matching_composed_char=True
		elif byte=="\xa4":
			print '''echo -ne "\\x05\\x00\\x00\\x30\\x00\\x00\\x00\\x00" > /dev/hidg0''' # CURRENCY SIGN
			found_matching_composed_char=True
		elif byte=="\xb5":
			print '''echo -ne "\\x20\\x00\\x00\\x32\\x00\\x00\\x00\\x00" > /dev/hidg0''' # MICRO SIGN
			found_matching_composed_char=True
		elif byte=="\xa7":
			#print '''echo -ne "\\x00\\x00\\x00\\x38\\x00\\x00\\x00\\x00" > /dev/hidg0''' # SECTION SIGN
			print '''echo -ne "\\x20\\x00\\x00\\x38\\x00\\x00\\x00\\x00" > /dev/hidg0''' # SECTION SIGN
			found_matching_composed_char=True
		elif byte=="\xb2":
			print '''echo -ne "\\x00\\x00\\x00\\x35\\x00\\x00\\x00\\x00" > /dev/hidg0''' # SUPERSCRIPT TWO
			found_matching_composed_char=True
		elif byte=="\xa7":
			found_matching_composed_char=True

	if found_matching_composed_char==True:
		print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''	
		global_last_char=""
		return True
	
	if ( byte=="\xc3" ) or ( byte=="\xc2" ):
		# We have a UTF-8 char
		global_last_char=byte;
		return True

	if byte=="\x21": print '''echo -ne "\\x00\\x00\\x00\\x38\\x00\\x00\\x00\\x00" > /dev/hidg0''' # !
	elif byte=="\x22": print '''echo -ne "\\x00\\x00\\x00\\x20\\x00\\x00\\x00\\x00" > /dev/hidg0''' # "
	elif byte=="\x23": print '''echo -ne "\\x05\\x00\\x00\\x20\\x00\\x00\\x00\\x00" > /dev/hidg0''' # #
	elif byte=="\x24": print '''echo -ne "\\x00\\x00\\x00\\x30\\x00\\x00\\x00\\x00" > /dev/hidg0''' # $
	elif byte=="\x25": print '''echo -ne "\\x20\\x00\\x00\\x34\\x00\\x00\\x00\\x00" > /dev/hidg0''' # %
	elif byte=="\x26": print '''echo -ne "\\x00\\x00\\x00\\x1e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # &
	elif byte=="\x27": print '''echo -ne "\\x00\\x00\\x00\\x21\\x00\\x00\\x00\\x00" > /dev/hidg0''' # '
	elif byte=="\x28": print '''echo -ne "\\x00\\x00\\x00\\x22\\x00\\x00\\x00\\x00" > /dev/hidg0''' # (
	elif byte=="\x2a": print '''echo -ne "\\x00\\x00\\x00\\x31\\x00\\x00\\x00\\x00" > /dev/hidg0''' # *
	#elif byte=="\x2a": print '''echo -ne "\\x00\\x00\\x00\\x32\\x00\\x00\\x00\\x00" > /dev/hidg0''' # *
	elif byte=="\x2b": print '''echo -ne "\\x20\\x00\\x00\\x2e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # +
	elif byte=="\x2c": print '''echo -ne "\\x00\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ,
	elif byte=="\x2d": print '''echo -ne "\\x00\\x00\\x00\\x23\\x00\\x00\\x00\\x00" > /dev/hidg0''' # -
	elif byte=="\x2e": print '''echo -ne "\\x20\\x00\\x00\\x36\\x00\\x00\\x00\\x00" > /dev/hidg0''' # .
	elif byte=="\x2f": print '''echo -ne "\\x20\\x00\\x00\\x37\\x00\\x00\\x00\\x00" > /dev/hidg0''' # /
	elif byte=="\x29": print '''echo -ne "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # )
	elif byte=="\x30": print '''echo -ne "\\x20\\x00\\x00\\x27\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 0
	elif byte=="\x31": print '''echo -ne "\\x20\\x00\\x00\\x1e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 1
	elif byte=="\x32": print '''echo -ne "\\x20\\x00\\x00\\x1f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 2
	elif byte=="\x33": print '''echo -ne "\\x20\\x00\\x00\\x20\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 3
	elif byte=="\x35": print '''echo -ne "\\x20\\x00\\x00\\x22\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 5
	elif byte=="\x36": print '''echo -ne "\\x20\\x00\\x00\\x23\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 6
	elif byte=="\x37": print '''echo -ne "\\x20\\x00\\x00\\x24\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 7
	elif byte=="\x38": print '''echo -ne "\\x20\\x00\\x00\\x25\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 8
	elif byte=="\x3a": print '''echo -ne "\\x00\\x00\\x00\\x37\\x00\\x00\\x00\\x00" > /dev/hidg0''' # :
	elif byte=="\x3b": print '''echo -ne "\\x00\\x00\\x00\\x36\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ;
	elif byte=="\x3c": print '''echo -ne "\\x00\\x00\\x00\\x64\\x00\\x00\\x00\\x00" > /dev/hidg0''' # <
	elif byte=="\x3d": print '''echo -ne "\\x00\\x00\\x00\\x2e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # =
	elif byte=="\x3e": print '''echo -ne "\\x20\\x00\\x00\\x64\\x00\\x00\\x00\\x00" > /dev/hidg0''' # >
	elif byte=="\x3f": print '''echo -ne "\\x20\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ?
	elif byte=="\x34": print '''echo -ne "\\x20\\x00\\x00\\x21\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 4
	elif byte=="\x39": print '''echo -ne "\\x20\\x00\\x00\\x26\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 9
	elif byte=="\x40": print '''echo -ne "\\x05\\x00\\x00\\x27\\x00\\x00\\x00\\x00" > /dev/hidg0''' # @
	elif byte=="\x41": print '''echo -ne "\\x20\\x00\\x00\\x14\\x00\\x00\\x00\\x00" > /dev/hidg0''' # A
	elif byte=="\x4d": print '''echo -ne "\\x20\\x00\\x00\\x33\\x00\\x00\\x00\\x00" > /dev/hidg0''' # M
	elif byte=="\x51": print '''echo -ne "\\x20\\x00\\x00\\x04\\x00\\x00\\x00\\x00" > /dev/hidg0''' # Q
	elif byte=="\x57": print '''echo -ne "\\x20\\x00\\x00\\x1d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # W
	elif byte=="\x5a": print '''echo -ne "\\x20\\x00\\x00\\x1a\\x00\\x00\\x00\\x00" > /dev/hidg0''' # Z
	elif byte=="\x5b": print '''echo -ne "\\x05\\x00\\x00\\x22\\x00\\x00\\x00\\x00" > /dev/hidg0''' # [
	elif byte=="\x5c": print '''echo -ne "\\x05\\x00\\x00\\x25\\x00\\x00\\x00\\x00" > /dev/hidg0''' # \
	elif byte=="\x5d": print '''echo -ne "\\x05\\x00\\x00\\x2d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ]
	elif byte=="\x5e": print '''echo -ne "\\x00\\x00\\x00\\x2f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ^
	#elif byte=="\x5e": print '''echo -ne "\\x05\\x00\\x00\\x26\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ^
	elif byte=="\x5f": print '''echo -ne "\\x00\\x00\\x00\\x25\\x00\\x00\\x00\\x00" > /dev/hidg0''' # _
	elif byte=="\x60": print '''echo -ne "\\x05\\x00\\x00\\x24\\x00\\x00\\x00\\x00" > /dev/hidg0''' # `
	elif byte=="\x61": print '''echo -ne "\\x00\\x00\\x00\\x14\\x00\\x00\\x00\\x00" > /dev/hidg0''' # a
	elif byte=="\x6d": print '''echo -ne "\\x00\\x00\\x00\\x33\\x00\\x00\\x00\\x00" > /dev/hidg0''' # m
	elif byte=="\x71": print '''echo -ne "\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x00" > /dev/hidg0''' # q
	elif byte=="\x77": print '''echo -ne "\\x00\\x00\\x00\\x1d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # w
	elif byte=="\x7a": print '''echo -ne "\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\x00" > /dev/hidg0''' # z
	elif byte=="\x7b": print '''echo -ne "\\x05\\x00\\x00\\x21\\x00\\x00\\x00\\x00" > /dev/hidg0''' # {
	elif byte=="\x7c": print '''echo -ne "\\x05\\x00\\x00\\x23\\x00\\x00\\x00\\x00" > /dev/hidg0''' # |
	elif byte=="\x7d": print '''echo -ne "\\x05\\x00\\x00\\x2e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # }
	elif byte=="\x7e": print '''echo -ne "\\x05\\x00\\x00\\x1f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ~
	else: return False
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''	
	return True


def findinlist(byte):
	if byte=="": return
	#print "#let's play with ["+byte +", "+''.join( [ "%02X " % ord( x ) for x in byte ] ).strip()+"]."
	if locale.getdefaultlocale()[0]=="fr_FR":
		# Special function call for French azerty keyboard
		if findinfrenchlist(byte) == True: 
			return
# Symbols 
	if   byte=="\x20": print '''echo -ne "\\x00\\x00\\x00\\x2c\\x00\\x00\\x00\\x00" > /dev/hidg0''' # SPACE
	elif byte=="\x21": print '''echo -ne "\\x20\\x00\\x00\\x1e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # !
	elif byte=="\x22": print '''echo -ne "\\x20\\x00\\x00\\x34\\x00\\x00\\x00\\x00" > /dev/hidg0''' # "
	elif byte=="\x23": print '''echo -ne "\\x20\\x00\\x00\\x20\\x00\\x00\\x00\\x00" > /dev/hidg0''' # #
	elif byte=="\x24": print '''echo -ne "\\x20\\x00\\x00\\x21\\x00\\x00\\x00\\x00" > /dev/hidg0''' # $
	elif byte=="\x25": print '''echo -ne "\\x20\\x00\\x00\\x22\\x00\\x00\\x00\\x00" > /dev/hidg0''' # %
	elif byte=="\x26": print '''echo -ne "\\x20\\x00\\x00\\x24\\x00\\x00\\x00\\x00" > /dev/hidg0''' # &
	elif byte=="\x27": print '''echo -ne "\\x00\\x00\\x00\\x34\\x00\\x00\\x00\\x00" > /dev/hidg0''' # '
	elif byte=="\x28": print '''echo -ne "\\x20\\x00\\x00\\x26\\x00\\x00\\x00\\x00" > /dev/hidg0''' # (
	elif byte=="\x29": print '''echo -ne "\\x20\\x00\\x00\\x27\\x00\\x00\\x00\\x00" > /dev/hidg0''' # )
	elif byte=="\x2a": print '''echo -ne "\\x20\\x00\\x00\\x25\\x00\\x00\\x00\\x00" > /dev/hidg0''' # *
	elif byte=="\x2b": print '''echo -ne "\\x20\\x00\\x00\\x2e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # +
	elif byte=="\x2c": print '''echo -ne "\\x00\\x00\\x00\\x36\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ,
	elif byte=="\x2d": print '''echo -ne "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # -
	elif byte=="\x2e": print '''echo -ne "\\x00\\x00\\x00\\x37\\x00\\x00\\x00\\x00" > /dev/hidg0''' # .
	elif byte=="\x2f": print '''echo -ne "\\x00\\x00\\x00\\x38\\x00\\x00\\x00\\x00" > /dev/hidg0''' # /
# Numbers
	elif byte=="\x30": print '''echo -ne "\\x00\\x00\\x00\\x27\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 0
	elif byte=="\x31": print '''echo -ne "\\x00\\x00\\x00\\x1e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 1
	elif byte=="\x32": print '''echo -ne "\\x00\\x00\\x00\\x1f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 2
	elif byte=="\x33": print '''echo -ne "\\x00\\x00\\x00\\x20\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 3
	elif byte=="\x34": print '''echo -ne "\\x00\\x00\\x00\\x21\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 4
	elif byte=="\x35": print '''echo -ne "\\x00\\x00\\x00\\x22\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 5
	elif byte=="\x36": print '''echo -ne "\\x00\\x00\\x00\\x23\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 6
	elif byte=="\x37": print '''echo -ne "\\x00\\x00\\x00\\x24\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 7
	elif byte=="\x38": print '''echo -ne "\\x00\\x00\\x00\\x25\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 8
	elif byte=="\x39": print '''echo -ne "\\x00\\x00\\x00\\x26\\x00\\x00\\x00\\x00" > /dev/hidg0''' # 9
# Symbols
	elif byte=="\x3a": print '''echo -ne "\\x20\\x00\\x00\\x33\\x00\\x00\\x00\\x00" > /dev/hidg0''' # :
	elif byte=="\x3b": print '''echo -ne "\\x00\\x00\\x00\\x33\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ;
	elif byte=="\x3c": print '''echo -ne "\\x20\\x00\\x00\\x36\\x00\\x00\\x00\\x00" > /dev/hidg0''' # <
	elif byte=="\x3d": print '''echo -ne "\\x00\\x00\\x00\\x2e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # =
	elif byte=="\x3e": print '''echo -ne "\\x20\\x00\\x00\\x37\\x00\\x00\\x00\\x00" > /dev/hidg0''' # >
	elif byte=="\x3f": print '''echo -ne "\\x20\\x00\\x00\\x38\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ?
	elif byte=="\x40": print '''echo -ne "\\x20\\x00\\x00\\x1f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # @
# Uppercase
	elif byte=="\x41": print '''echo -ne "\\x20\\x00\\x00\\x04\\x00\\x00\\x00\\x00" > /dev/hidg0''' # A
	elif byte=="\x42": print '''echo -ne "\\x20\\x00\\x00\\x05\\x00\\x00\\x00\\x00" > /dev/hidg0''' # B
	elif byte=="\x43": print '''echo -ne "\\x20\\x00\\x00\\x06\\x00\\x00\\x00\\x00" > /dev/hidg0''' # C
	elif byte=="\x44": print '''echo -ne "\\x20\\x00\\x00\\x07\\x00\\x00\\x00\\x00" > /dev/hidg0''' # D
	elif byte=="\x45": print '''echo -ne "\\x20\\x00\\x00\\x08\\x00\\x00\\x00\\x00" > /dev/hidg0''' # E
	elif byte=="\x46": print '''echo -ne "\\x20\\x00\\x00\\x09\\x00\\x00\\x00\\x00" > /dev/hidg0''' # F
	elif byte=="\x47": print '''echo -ne "\\x20\\x00\\x00\\x0a\\x00\\x00\\x00\\x00" > /dev/hidg0''' # G
	elif byte=="\x48": print '''echo -ne "\\x20\\x00\\x00\\x0b\\x00\\x00\\x00\\x00" > /dev/hidg0''' # H
	elif byte=="\x49": print '''echo -ne "\\x20\\x00\\x00\\x0c\\x00\\x00\\x00\\x00" > /dev/hidg0''' # I
	elif byte=="\x4a": print '''echo -ne "\\x20\\x00\\x00\\x0d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # J
	elif byte=="\x4b": print '''echo -ne "\\x20\\x00\\x00\\x0e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # K
	elif byte=="\x4c": print '''echo -ne "\\x20\\x00\\x00\\x0f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # L
	elif byte=="\x4d": print '''echo -ne "\\x20\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0''' # M 
	elif byte=="\x4e": print '''echo -ne "\\x20\\x00\\x00\\x11\\x00\\x00\\x00\\x00" > /dev/hidg0''' # N
	elif byte=="\x4f": print '''echo -ne "\\x20\\x00\\x00\\x12\\x00\\x00\\x00\\x00" > /dev/hidg0''' # O
	elif byte=="\x50": print '''echo -ne "\\x20\\x00\\x00\\x13\\x00\\x00\\x00\\x00" > /dev/hidg0''' # P
	elif byte=="\x51": print '''echo -ne "\\x20\\x00\\x00\\x14\\x00\\x00\\x00\\x00" > /dev/hidg0''' # Q
	elif byte=="\x52": print '''echo -ne "\\x20\\x00\\x00\\x15\\x00\\x00\\x00\\x00" > /dev/hidg0''' # R
	elif byte=="\x53": print '''echo -ne "\\x20\\x00\\x00\\x16\\x00\\x00\\x00\\x00" > /dev/hidg0''' # S
	elif byte=="\x54": print '''echo -ne "\\x20\\x00\\x00\\x17\\x00\\x00\\x00\\x00" > /dev/hidg0''' # T
	elif byte=="\x55": print '''echo -ne "\\x20\\x00\\x00\\x18\\x00\\x00\\x00\\x00" > /dev/hidg0''' # U
	elif byte=="\x56": print '''echo -ne "\\x20\\x00\\x00\\x19\\x00\\x00\\x00\\x00" > /dev/hidg0''' # V
	elif byte=="\x57": print '''echo -ne "\\x20\\x00\\x00\\x1a\\x00\\x00\\x00\\x00" > /dev/hidg0''' # W
	elif byte=="\x58": print '''echo -ne "\\x20\\x00\\x00\\x1b\\x00\\x00\\x00\\x00" > /dev/hidg0''' # X
	elif byte=="\x59": print '''echo -ne "\\x20\\x00\\x00\\x1c\\x00\\x00\\x00\\x00" > /dev/hidg0''' # Y
	elif byte=="\x5a": print '''echo -ne "\\x20\\x00\\x00\\x1d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # Z
# Symbols
	elif byte=="\x5b": print '''echo -ne "\\x00\\x00\\x00\\x2f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # [
	elif byte=="\x5c": print '''echo -ne "\\x00\\x00\\x00\\x31\\x00\\x00\\x00\\x00" > /dev/hidg0''' # \ 
	elif byte=="\x5d": print '''echo -ne "\\x00\\x00\\x00\\x30\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ]
	elif byte=="\x5e": print '''echo -ne "\\x20\\x00\\x00\\x23\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ^
	elif byte=="\x5f": print '''echo -ne "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # _
	elif byte=="\x60": print '''echo -ne "\\x00\\x00\\x00\\x35\\x00\\x00\\x00\\x00" > /dev/hidg0''' # `
# Lowercase
	elif byte=="\x61": print '''echo -ne "\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x00" > /dev/hidg0''' # a
	elif byte=="\x62": print '''echo -ne "\\x00\\x00\\x00\\x05\\x00\\x00\\x00\\x00" > /dev/hidg0''' # b
	elif byte=="\x63": print '''echo -ne "\\x00\\x00\\x00\\x06\\x00\\x00\\x00\\x00" > /dev/hidg0''' # c
	elif byte=="\x64": print '''echo -ne "\\x00\\x00\\x00\\x07\\x00\\x00\\x00\\x00" > /dev/hidg0''' # d
	elif byte=="\x65": print '''echo -ne "\\x00\\x00\\x00\\x08\\x00\\x00\\x00\\x00" > /dev/hidg0''' # e
	elif byte=="\x66": print '''echo -ne "\\x00\\x00\\x00\\x09\\x00\\x00\\x00\\x00" > /dev/hidg0''' # f
	elif byte=="\x67": print '''echo -ne "\\x00\\x00\\x00\\x0a\\x00\\x00\\x00\\x00" > /dev/hidg0''' # g
	elif byte=="\x68": print '''echo -ne "\\x00\\x00\\x00\\x0b\\x00\\x00\\x00\\x00" > /dev/hidg0''' # h
	elif byte=="\x69": print '''echo -ne "\\x00\\x00\\x00\\x0c\\x00\\x00\\x00\\x00" > /dev/hidg0''' # i
	elif byte=="\x6a": print '''echo -ne "\\x00\\x00\\x00\\x0d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # j
	elif byte=="\x6b": print '''echo -ne "\\x00\\x00\\x00\\x0e\\x00\\x00\\x00\\x00" > /dev/hidg0''' # k
	elif byte=="\x6c": print '''echo -ne "\\x00\\x00\\x00\\x0f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # l
	elif byte=="\x6d": print '''echo -ne "\\x00\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0''' # m
	elif byte=="\x6e": print '''echo -ne "\\x00\\x00\\x00\\x11\\x00\\x00\\x00\\x00" > /dev/hidg0''' # n
	elif byte=="\x6f": print '''echo -ne "\\x00\\x00\\x00\\x12\\x00\\x00\\x00\\x00" > /dev/hidg0''' # o
	elif byte=="\x70": print '''echo -ne "\\x00\\x00\\x00\\x13\\x00\\x00\\x00\\x00" > /dev/hidg0''' # p
	elif byte=="\x71": print '''echo -ne "\\x00\\x00\\x00\\x14\\x00\\x00\\x00\\x00" > /dev/hidg0''' # q
	elif byte=="\x72": print '''echo -ne "\\x00\\x00\\x00\\x15\\x00\\x00\\x00\\x00" > /dev/hidg0''' # r
	elif byte=="\x73": print '''echo -ne "\\x00\\x00\\x00\\x16\\x00\\x00\\x00\\x00" > /dev/hidg0''' # s
	elif byte=="\x74": print '''echo -ne "\\x00\\x00\\x00\\x17\\x00\\x00\\x00\\x00" > /dev/hidg0''' # t
	elif byte=="\x75": print '''echo -ne "\\x00\\x00\\x00\\x18\\x00\\x00\\x00\\x00" > /dev/hidg0''' # u
	elif byte=="\x76": print '''echo -ne "\\x00\\x00\\x00\\x19\\x00\\x00\\x00\\x00" > /dev/hidg0''' # v
	elif byte=="\x77": print '''echo -ne "\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\x00" > /dev/hidg0''' # w
	elif byte=="\x78": print '''echo -ne "\\x00\\x00\\x00\\x1b\\x00\\x00\\x00\\x00" > /dev/hidg0''' # x
	elif byte=="\x79": print '''echo -ne "\\x00\\x00\\x00\\x1c\\x00\\x00\\x00\\x00" > /dev/hidg0''' # y
	elif byte=="\x7a": print '''echo -ne "\\x00\\x00\\x00\\x1d\\x00\\x00\\x00\\x00" > /dev/hidg0''' # z
#Shift chars
	elif byte=="\x7b": print '''echo -ne "\\x20\\x00\\x00\\x2f\\x00\\x00\\x00\\x00" > /dev/hidg0''' # {
	elif byte=="\x7c": print '''echo -ne "\\x20\\x00\\x00\\x31\\x00\\x00\\x00\\x00" > /dev/hidg0''' # | 
	elif byte=="\x7d": print '''echo -ne "\\x20\\x00\\x00\\x30\\x00\\x00\\x00\\x00" > /dev/hidg0''' # }
	elif byte=="\x7e": print '''echo -ne "\\x00\\x00\\x00\\x40\\x00\\x00\\x00\\x00" > /dev/hidg0''' # ~ 
#SDLK_RETURN,0x28
	elif byte=="\x0a": print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x0d": print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
#SDLK_ESCAPE,0x29
#SDLK_BACKSPACE,0x2a
#SDLK_TAB,0x2b
	else: print "#crap, couldn't find ["+byte +"]. Perhaps try adding it to the list."
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''	

def wincmd():
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	findinlist('c')
	print '''sleep 1'''
	findinlist('m')
	print '''sleep 1'''
	findinlist('d')
	print '''sleep 1'''
	print '''echo -ne "\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x20\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	enterb()
	print '''sleep 3'''

def win7cmd_elevated():
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	findinlist('c')
	print '''sleep 1'''
	findinlist('m')
	print '''sleep 1'''
	findinlist('d')
	print '''sleep 1'''
	print '''echo --left-ctrl --left-shift --return | hid-keyboard /dev/hidg0 keyboard'''
	print '''sleep 1'''
	print '''echo --left-alt y | hid-keyboard /dev/hidg0 keyboard'''
	print '''sleep 3'''

def win8cmd_elevated():
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	findinlist('c')
	print '''sleep 1'''
	findinlist('m')
	print '''sleep 1'''
	findinlist('d')
	print '''sleep 1'''
	print '''echo -ne "\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x02\\x00\\x00\\x43\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	enterb()
	print '''sleep 2'''
	print '''echo -ne "\\x04\\x00\\x00\\x1c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 3'''

def enterb():
	print '''sleep 2'''
	print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''


