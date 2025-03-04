#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys                

def find_position(char):
  for set_num in range(len(table)):
    if char in table[set_num]:
      return set_num
  return False

def forge_offsets(string, direction, offset):
  if type(string) is str:
    return [((ord(x) - 96) + offset) * direction for x in string]
  else:
    return [(x + offset) * direction for x in string]

def frequency(text):
  return {letter: text.count(letter) for letter in 'abcdefghijklmnopqrstuvwxyz'.upper()}

######
#
#  Scroll down for the bits you should interact with
#
######

#
# If it doesn't make sense your best shot is to either read the code or just go with it
#

# List of possible parameters
dict = ["own", "p0","p1","p2","p3","p4","p5","p6","p7","p8","p9","p10","p11","p12","p13","p14","p15","p16","p17","p18","p19","p20","p21","p22","p23","p24","p25","p26","p27","p28","p29",
	"p30","p31","p32","p33", "p34","p35","p36","p37","p38","p39","p40","p41","p42","p43","p44","p45","p46","p47","p48","p49","p51","p52","p53","p54","p55","p56","p57"]

# Here we have the 'offsets' 
# e.g. If you have [2, 3, 5, 7] you'll shift the first rune by 2, the second by 3, etc
#
# To invalidate one sequence put a # before it, to validate delete the #, leave all others with a # before it
#
# The first instance of 'offsets' below will work on page 56
# The second instance works on page 57, and also any runes that are in plaintext
# The third and fourth are totient sequence and totient of primes sequence respectively
# The fifth sequence is just a parameter to avoid destroying other sequences

# Primes
# sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987]

# Empty sequence
sequence = [0 for x in range(1000)]

# Totient
# sequence = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44, 24, 70, 24, 72, 36, 40, 36, 60, 24, 78, 32, 54, 40, 82, 24, 64, 42, 56, 40, 88, 24, 72, 44, 60, 46, 72, 32, 96, 42, 60, 40, 100, 32, 102, 48, 48, 52, 106, 36, 108, 40, 72, 48, 112, 36, 88, 56, 72, 58, 96, 32, 110, 60, 80, 60, 100, 36, 126, 64, 84, 48, 130, 40, 108, 66, 72, 64, 136, 44, 138, 48, 92, 70, 120, 48, 112, 72, 84, 72, 148, 40, 150, 72, 96, 60, 120, 48, 156, 78, 104, 64, 132, 54, 162, 80, 80, 82, 166, 48, 156, 64, 108, 84, 172, 56, 120, 80, 116, 88, 178, 48, 180, 72, 120, 88, 144, 60, 160, 92, 108, 72, 190, 64, 192, 96, 96, 84, 196, 60, 198, 80, 132, 100, 168, 64, 160, 102, 132, 96, 180, 48, 210, 104, 140, 106, 168, 72, 180, 108, 144, 80, 192, 72, 222, 96, 120, 112, 226, 72, 228, 88, 120, 112, 232, 72, 184, 116, 156, 96, 238, 64, 240, 110, 162, 120, 168, 80, 216, 120, 164, 100, 250, 72, 220, 126, 128, 128, 256, 84, 216, 96, 168, 130, 262, 80, 208, 108, 176, 132, 268, 72, 270, 128, 144, 136, 200, 88, 276, 138, 180, 96, 280, 92, 282, 140, 144, 120, 240, 96, 272, 112, 192, 144, 292, 84, 232, 144, 180, 148, 264, 80, 252, 150, 200, 144, 240, 96, 306, 120, 204, 120, 310, 96, 312, 156, 144, 156, 316, 104, 280, 128, 212, 132, 288, 108, 240, 162, 216, 160, 276, 80, 330, 164, 216, 166, 264, 96, 336, 156, 224, 128, 300, 108, 294, 168, 176, 172, 346, 112, 348, 120, 216, 160, 352, 116, 280, 176, 192, 178, 358, 96, 342, 180, 220, 144, 288, 120, 366, 176, 240, 144, 312, 120, 372, 160, 200, 184, 336, 108, 378, 144, 252, 190, 382, 128, 240, 192, 252, 192, 388, 96, 352, 168, 260, 196, 312, 120, 396, 198, 216, 160, 400, 132, 360, 200, 216, 168, 360, 128, 408, 160, 272, 204, 348, 132, 328, 192, 276, 180, 418, 96, 420, 210, 276, 208, 320, 140, 360, 212, 240, 168, 430, 144, 432, 180, 224, 216, 396, 144, 438, 160, 252, 192, 442, 144, 352, 222, 296, 192, 448, 120, 400, 224, 300, 226, 288, 144, 456, 228, 288, 176, 460, 120, 462, 224, 240, 232, 466, 144, 396, 184, 312, 232, 420, 156, 360, 192, 312, 238, 478, 128, 432, 240, 264, 220, 384, 162, 486, 240, 324, 168, 490, 160, 448, 216, 240, 240, 420, 164, 498, 200]

# Totient of Primes
# sequence = [1, 2, 4, 6, 10, 12, 16, 18, 22, 28, 30, 36, 40, 42, 46, 52, 58, 60, 66, 70, 72, 78, 82, 88, 96, 100, 102, 106, 108, 112, 126, 130, 136, 138, 148, 150, 156, 162, 166, 172, 178, 180, 190, 192, 196, 198, 210, 222, 226, 228, 232, 238, 240, 250, 256, 262, 268, 270, 276, 280, 282, 292, 306, 310, 312, 316, 330, 336, 346, 348, 352, 358, 366, 372, 378, 382, 388, 396, 400, 408, 418, 420, 430, 432, 438, 442, 448, 456, 460, 462, 466, 478, 486, 490, 498, 502, 508, 520, 522, 540, 546, 556, 562, 568, 570, 576, 586, 592, 598, 600, 606, 612, 616, 618, 630, 640, 642, 646, 652, 658, 660, 672, 676, 682, 690, 700, 708, 718, 726, 732, 738, 742, 750, 756, 760, 768, 772, 786, 796, 808, 810, 820, 822, 826, 828, 838, 852, 856, 858, 862, 876, 880, 882, 886, 906, 910, 918, 928, 936, 940, 946, 952, 966, 970, 976, 982, 990, 996, 1008, 1012, 1018, 1020, 1030, 1032, 1038, 1048, 1050, 1060, 1062, 1068, 1086, 1090, 1092, 1096, 1102, 1108, 1116, 1122, 1128, 1150, 1152, 1162, 1170, 1180, 1186, 1192, 1200, 1212, 1216, 1222, 1228, 1230, 1236, 1248, 1258, 1276, 1278, 1282, 1288, 1290, 1296, 1300, 1302, 1306, 1318, 1320, 1326, 1360, 1366, 1372, 1380, 1398, 1408, 1422, 1426, 1428, 1432, 1438, 1446, 1450, 1452, 1458, 1470, 1480, 1482, 1486, 1488, 1492, 1498, 1510, 1522, 1530, 1542, 1548, 1552, 1558, 1566, 1570, 1578, 1582, 1596, 1600, 1606, 1608, 1612, 1618, 1620, 1626, 1636, 1656, 1662, 1666, 1668, 1692, 1696, 1698, 1708, 1720, 1722, 1732, 1740, 1746, 1752, 1758, 1776, 1782, 1786, 1788, 1800, 1810, 1822, 1830, 1846, 1860, 1866, 1870, 1872, 1876, 1878, 1888, 1900, 1906, 1912, 1930, 1932, 1948, 1950, 1972, 1978, 1986]

# Your sequence
# sequence = []

table = [
  ["ᚠ", "F"], 
  ["ᚢ", "V"],
  ["ᚦ", "TH"],
  ["ᚩ", "O"],
  ["ᚱ", "R"],
  ["ᚳ", "C"],
  ["ᚷ", "G"],
  ["ᚹ", "W"],
  ["ᚻ", "H"],
  ["ᚾ", "N"],
  ["ᛁ", "I"],
  ["ᛂ", "J"],
  ["ᛇ", "EO"],
  ["ᛈ", "P"],
  ["ᛉ", "X"],
  ["ᛋ", "S"],
  ["ᛏ", "T"],
  ["ᛒ", "B"],
  ["ᛖ", "E"],
  ["ᛗ", "M"],
  ["ᛚ", "L"],
  ["ᛝ", "ING"],
  ["ᛟ", "OE"],
  ["ᛞ", "D"],
  ["ᚪ", "A"],
  ["ᚫ", "AE"],
  ["ᚣ", "Y"],
  ["ᛡ", "IA"],
  ["ᛠ", "EA"]
]

# Always keep in mind that these runes comes from http://titanpad.com/hJ8pVQ5S43 so if this link contains any errors
# this script will have it too. If any error is found, fix then reupload it, please
#
# All blocks down are all pages in runes coded by p* where * is the number of page (0-57)
# p50 does not exists because it has no runes
#
# The collection of all pages is called book and it is stored in an array
#
# The "own" page is a page that you may use it to test anything you want, to avoid destroying
# the other pages
# 
# Note that in page 56, there is an 'F' in plaintext. The cipher skips over this completely.
# I have replaced it with three spaces. 
# If you want it back for sake of completeness, replace those three spaces with ᚠ

book = [
	# Your own text
	""" """,

	# p0
	"""ᛋᚻᛖᚩᚷᛗᛡᚠ•ᛋᚣᛖᛝᚳ•ᚦᛂᚷᚫ•ᚠᛂᛟ•
	ᚩᚾᚦ•ᚾᛖᚹᛒᚪᛋᛟᛇᛁᛝᚢ•ᚾᚫᚷᛁᚦ•ᚻᛒᚾᛡ•
	ᛈᛒᚾ•ᛇᛂᚦ•ᚪᛝᚣᛉ•ᛒᛞᛈ•ᛖᛡᚠᛉᚷᚠ•
	ᛋᛈᛏᚠᛈᚢᛝᚣᛝᛉᛡ•ᚣᚻ•ᛒᚢ•ᚷᚩᛈ•ᛝᚫᚦ•ᛁ
	ᚫᚻᛉᚦᛈᚷ•ᚣᚠᛝᚳᛂ•ᚦᚪᛗᛁᛝᛁᛡᚣ•ᚻᛇ•ᛏᚻᚫ
	ᛡ•ᛉᚣ•ᛖᚢᛝ•ᚳᚠᚾᚦ•ᚦᛈ•ᚣᛝᛠ•ᚣᚾ
	ᛖᚣ•ᛞᛉᛝ•ᚠᛚᚹᛇᛏᚠᚷᚾ•ᛗᛇᛚᚾ•
	ᛝᛗᚠᚱᛡ•ᚪᛋ•ᛠᛗᛝᛉᛉᛇᛞᛒ•ᛟᛞᛗᚩ•ᛠ
	ᛇᚻ•ᛞᛝᚷ•ᛟᛝᛚᚢᚱᚾᛏ•ᚫᛋᚣᚢᚻᚱᛏ•ᚻᚳ•ᛋᛟ
	ᛏᛟᛝᚢᚱ•ᛋ•ᚠᚩᛖᚹᛠᛟᛚᚠᚫ•ᛗᚱᛝ•ᛞᚪᛗᚱ•ᚹ""",
	
	# p1
	"""ᚪᛁᛗᛋᚾ•ᛋᛟᚱᚢᚹᛋᛚᛡ•ᛟᚪᚫᛝᛋᛞᛈᛏ•ᚳᚱᚦ
	ᛡ•ᚱᛒᚩᛞᚦᚠ•ᚣᛉᛁᛏ•ᛟᛁ•ᚠᛚᚩ•ᚠᛠ•ᚱᚩᛟᛗᚻ
	ᛗᚷᛈᚻ•ᚫᚻᚾᚩᚻᚣ•ᛟᛋᛚ•ᚾᚷ•ᚫᚣ•ᛟᚳᛒᛚᛂ•ᛝ
	ᛚᛟ•ᚫᛂᛠᚹ•ᛠᚦᚩ•ᛒᛟᚣ•ᚳᚠᚳᛂ•ᛚᚫ•ᚾ•ᚦᛈ•
	ᚢᛉ•ᛟᛉᚷ•ᛈᚠᛋᛇᚫᛟ•ᛝᛈᛇᚩᛖᚪ•ᚷᚫᛡᛝᚦᚩ
	•ᛈᚪᛟᚦᚱᛝᚫ•ᚳᛋᛒᛇᚣᚻ•ᛏᛉᛖᛚᚱ•ᚷᚹᚣ•ᛂᚠ
	ᛁᚾᛡᚳᚣᛠᛁᛡ•ᚩᚦ•ᛖᚳᚫᚳᛉᛡᛠ•ᚩᛚᚳ•ᚠᚱ
	ᛞᛝᛖᚢ•ᛞᚳᛚᛠᛋᛉᚳᚷᛡ•ᚹᛋᚦ•ᚠᛞᛝ•ᛁᛡ
	ᛗᚪᚫᚷ•ᚹᛋ•ᚾᛞ•ᚳᛈᚦᛉᛈᛠᛠ•ᚹᚢ•ᛠᚹ•ᚠᚹ
	ᛂᚣ•ᛉᛞᚹᚳᚷᚳᛟ•ᛞᛉᛟ•ᚱᛡᚷ•ᚾᛈᚪᚣᛈ•ᚳ
	ᚣᚻ•ᚠᛖᛂᛠᚾ•ᛟᚫ•ᚢᚪ•ᚻᚱ•ᛖᛠᚦᚠᛂᚪ•ᛚᛉ
	ᛋᛏ•ᛗᚠᛚᚠᛏ•ᚷᛁᚦ•ᚢᛚᚷ•ᛉᛠᛏᛋᛚᛂᛈ•ᛚᛉᛁ""",

	# p2
	"""ᛟᛗ•ᚢ•ᚻᛏ•ᛒᛇᛚᛞᚻᛒᛗ•ᛠᚱᛒ•ᚾᚻᛒᛖᚷᛇ•
	ᛞᛚᚹᛇᛡᛈᚩ•ᚻᛖᛠ•ᚹᛁᚱᛁᚻ•ᚢᚦᚻᚣ•ᚾᛉᛒᚷᛂ
	ᛈᚢ•ᛝᛠᚠᚾᛁᛖᛞᛡᛝᚱ•ᛞᛒᛂᛡᛟᛗᛁ•ᚠᛏ•ᛂ
	ᛞᛁᚦᚱᛚᛋ•ᛖᛇᚩᚷᛒᛏᛞ•ᚦᚪᚾᚳᚣ•ᛡᛋᚦᛞ•ᛝᚠᛚ
	ᛖᚷᚻᚳ•ᛖᚩᛁᛏᚾᛉ•ᛈᛏᚠᚻᚱᛞᛖᚠᛏ•ᚫᚹᚻ•ᛒ
	ᚳ•ᚠ•ᛈᚪᛚᚢᛠᚾᛚᛂ•ᛂᚳᛚᚹᛠᛞᚢᛞᛇ•ᛠᛉ
	ᛞᚹᚻᛠ•ᚦᛡᚫᚳᛚᛏᚹᛖᛁᚳ•ᛈᛟᛞᚳ•ᚾᚻᚪ•ᚱᛁᚷ
	ᚦᛠᛖᛏᚷ•ᚦᚻᚩᛡᚹᚫᛂᛖ•ᛝᛠᛞ•ᚩᚫ•ᚪᛚ•ᛒᛂ
	ᚳᚢᛉᛏᚪᛒᛂᛈ•ᚠᛠ•ᚻᛞᚾᛡᚢᛈᛋᚢᚹ•""",
	
	# p3 
	"""ᛚᛂ•ᛇᚻᛝᚳᚦᛏᚫᛂᛏᛉᚻ•ᛏᚢᛟ•ᛋᛈᚱᚷ
	•ᚣᚾᚪᚷᛇᛝᚾ•ᚹᚠᚣᚾᛒᛠᛡ•ᛈᚾᚣᚪᛋᛗ
	ᛒ•ᛡᛠᛡᛁ•ᚩᛒᚱᚾᛚᛠ•ᚱᛚᛚᛖᚠ
	ᛟᛒ•ᛝ•ᚱᚪᛡᚷᛟᛇᛏᛗᛉ•ᛞᛇ•ᛗᚣᚻᛠ•ᛁᛚᛋ•ᚾ
	ᚹᚳᚠᛈᛗᛈᛚ•ᛠᛋᚦᚠᛟᛡ•ᚦᛖᚣ•ᚳᛂᛚᚳᛡᛗ•
	ᛒᛞᚳᛇ•ᛂᛁᛏᛟ•ᛞᛠᛖᛡᚾᛏ•
	ᛈᛞᚦ•ᛇᛞᛇ•ᚫᛚᚳ•ᛡᛇ•ᛠᚻ•ᚹᛗᚣᚦ
	ᚢ•ᚻᛏᚦᚱᚻᛝ•ᛚᛝᛋ•ᚾᚫᛠᚷᛋᛚ•ᛋᛉ
	ᚩᚻᚹᛞᛗᛖᛗᚪᚠ•ᚳᚣᚳᚫᚾ•ᛏᚦᚷ•ᛁᛂᛁ
	•ᚳᛞᛡᛉ•ᚻᚫᚫᛠᚷ•ᛠᛝ•ᚠᛏᚩᚱᛞᚳᛇ•ᚠᚢ
	ᛉᛠᛒᚩ•ᛉᛁᚣᚷᛋᛋᛒᛠ•ᚩᛁᛈ•ᛁᛂᛁᚩᛖ•ᚻᛠᚻ""",
	
	# p4
	"""ᛚᛡ•ᚣᛈᛉᛁᚹᛗᚳᛁ•ᛚᚷᚠᚾᛡᚳᛉ•ᛈᚩᚱᛡ•ᚻ•ᛂ
	ᛗ•ᛟᛉᛝ•ᚢᛗᛇᛠᚷᛝ•ᛝᚹᚳ•ᛚᛝᚢ•ᛉᛂᚠᛟ
	ᚢ•ᚷᛠ•ᛗᛉ•ᚪᚹ•ᛚᚢᛉᚫ•ᛗᛞᛝᚻᚱᚣ•ᚻᚪ•ᚷᛁ
	ᚠᚷᚳ•ᚫᛝᛂᛇᛉᛡ•ᚾᚦᛒᚢᛂᚱ•ᚹ•ᚷᛚᛟᚷ•ᚦᛇᚠ•
	ᚦᛠᛁ•ᛋᚷ•ᚷᚣ•ᛠᛡᛈ•ᛡᚫᛚ•ᚦᛠᛉᚫ•ᛖᛗ
	ᛖᛏᛟᛏ•ᛠᚳᚠ•ᚳᛠᚷ•ᚦ•ᛈᛁᚳᚾ•ᛇᚣᛝᛂᛝ
	ᛗᚹᚳᚾ•ᛒᚣᛠ•ᚩᛟᚷᚱ•ᛗᚱᛗᛈᛡᚹ•ᚫᛟᚦᛟ•ᛈ
	ᛉᛂᛚ•ᚱᛚᚱᛒᚪᛈᛏᛉᛚᛏ•ᛗᛉᛁ'ᚹ•ᛂᛋᛟᛗᚾᚱ
	ᛖᛒᛋ•ᚳᛏᛚᛟ•ᛋᛒᚠᛉᚦᚪᛠᚢ•ᛇᛉ•ᚱᚷᛏᛇᛠ
	ᛁᛂᛒᛟ•ᛉᚷᛂᛝ•ᛠᚦ•ᚱᛝᛒ•ᚾᚢᚪᛝᛒᛈᛋᛠ•ᛈ
	ᚹᚩᚻᛖ•ᚫᛇᚷᚾᚫᛋᛇ•ᚩᛈᛗ•ᛖᛉᛡᛒᚹ•ᚢᛖᛁᛞ•
	ᛈᚪᛇᚷᛋᚳᚷᛞᛈᚣ•ᛡᛚᚦᚱ•ᚳᚢᚠᛇᚦ•ᛉᛖᛚ•ᚢ""",
	
	# p5
	"""ᚱᚫ•ᛉᚻᛂᚫᛗᛚᚠ•ᚳᛝᛞ•ᛁᛝᚩ•ᚳᛋᛟᛖᚣᛟᚻᚢ•
	ᚷᛞᚹᚪ•ᛖᛋᚷᛝᚠᛉ•ᛞᛉᛂ•ᛠᚻᛁ•ᚦᛈᛉᚣ•ᛡ•
	ᛇᛞᛇᛝᛇᛝ•ᛖᛠᛞᚱ•ᛚᛇᛏ•ᛉᛏᚣ•ᚱᛇ•ᛈᛝᛇ
	ᛈᚩᛁᛚᛖᚠ•ᛇᚫᚪ•ᚣᛝᚠᚣ•ᚠᛞᚾᛚ•ᛉᛏᚾᚫᛋ•ᛁᚩ
	ᚳᚢ•ᚣᛠᚾᛏᚷᚳᚪ•ᛉᛡᛇ•ᚦᛂᚣᛂᛚᛟᛖᛚ•ᚣ•
	•ᛈᛡ•ᛖᚹᛟ•ᛇᚾᚪ•ᚻᛞᛇᛋ•ᚦᚣᛇᚦᛂᚦᚱᚢ•ᚳᛠ
	ᚪ•ᚢᛂᛡᛈ•ᚣᚫᛇᛋ•ᚻᛠᛏᚣᛞᚣᚫᚠᚻᚩ•ᛟᛗ
	ᛉᛟᛂᚷ•ᚢᛡᚱᛡᚳ•ᛁᚠᛟ•ᛁᛂᛈᛒ•ᛖᛝᚣᚦᚩᚫᚣ•
	ᛠᛉᛡᛖᛚ•ᛁᚱᚣᛞᛠᛂ•ᚫᚳ•ᛗᚷᛁᚫᚢᚪᚫ•ᛂᚪ
	ᚻᛈ•ᚠᛞᛚᛁᛠᛈᛟᚣᚩ•ᚢᛒᚷᛝᛟᚢᛝᛋᚢᚳ•ᛏ
	ᛞ•ᚫᛈᚩᛂ•ᛒᚻᚱᛁᚷᚻᛂ•ᚣᚹᛗᛇᚾᚫ•ᛞᛝᛇ•ᛟᛂ
	ᛝᚳᛖᛠ•ᛉᚪᚱᚣ•ᚪᚢᛏ•ᚳᛈᚳ•ᚩᛇᛟ•ᚫᛈ•ᛏ""",
	
	# p6
	"""ᛉᚳᚻᛞᛇ•ᛉᛒᛠ•ᚫᚾᛂ•ᛠᚪᛒ•ᛖᛠᚹ•ᛡᛚ•
	ᚹᛁᛡᛋᛈᛚᚦᚪᛋᛂ•ᛡᛞᚣᚱᛞᛟ•ᚦᚱᛉᛟᚹ•ᚣᛞᛏ•
	ᚷᛚᛡᚻᚹᛗᚱ•ᛝᚠᚳ•ᚱᚫᛁᛒᚷᛈᚣ•ᛞᚪᚱᚪᛉᛟ•ᚢ
	ᚩᛁᛠ•
	ᚪᛏᛉᛒ•ᛗ•ᚷᛡᛋᛒ•ᛉᛇ•ᚷᚾᛠᚫᚷᛝᛞ•
	ᛉᛖᛏᚩᚷᛡ•ᛝᚻᛏ•ᚳᛁᚣ•ᛂᛏ•ᛟᚩᚻᚱᛂ•
	ᚳᛖᛡᚩ•ᛞᚪᛏᚣᚢᚾᚱᛇ•ᚫᚫᛁᛖᚠᛝᚦᚻ•
	ᛉᛁᛟᛋᛁ•ᛗᚪ•ᚢᛂᚳᛋᚹᚾᚣ•ᚩᛈᛉᚱ•ᛚᚫᛟᛏᛡ•ᛂ
	ᛈᛗ•ᛞᛋᚠᛗ•ᛟᚹ•ᛞᛚᛏ•ᚷᚱ•ᚩᚢᛋᚻᚪ•ᚣᛇᛡᛚ
	ᚢᚻ•ᛈᚹᛂᛚᚷᛒ•ᛗᚢᛂᛗ•ᛇᚾᛇ•"ᚫᛚᚪᛚᚷᚪ•ᛋ""",
	
	# p7
	"""ᚻᛝ•ᛚᚦᛒ•ᛋᚳᚢᚳᚩᛡ"•ᛚᚳᛂ•ᛉᚪᚾᛇᛉ•ᛠ
	ᛗᛈᚢ•ᛗᚠᛚᛠᛝ•ᛒᛉᛁ•ᛚᚦᚱ•ᛠᛡᛁᚳ•ᚩᛉᛖ
	ᛞᛡ•ᛏᛋᛗᛠᛂᛈ•ᛠᛟ•ᛡᚫᚦᚹᚻᛈᛇᚪᚷᛈᚻ
	ᛠ•ᚳᛚᛠᛈ•ᛡᚣᚾᛁ•ᛚᛡᛁᚳ•ᚫᛇᚾ•ᚫᚳᛡᚱᛡᛚ
	ᛞ•ᛒᛟᛝᛡ•ᛉᛗᛝ•ᚳᚻᛟᛠᚾᛈᚳᚦ•ᛁᛇᚦ•ᛇᚢᚩ
	•ᚦᛈᚪ•ᛡᛚᛟᚹᛡᛈ•ᛂᛗ•ᚷᛒᛈᛋᚾᛇ•ᛏᚩᚷᚢᚾᚫ
	ᛖ•ᚾᚣᛁᛖ•ᛞᛝ•ᛞᛝ•ᛚᚢᛚᛉ•ᚪᚾᛝ•ᛇᚪᛂ•ᚻ•ᛞ
	ᚹᛈᚫᚹᚫ•ᛇᛁᛚᛝ•ᚦᚾᚳ•ᛒᛁᛏ•ᛠᚳᚩᛇᛖᛝ•ᚳᚻ
	ᛟᚻᚫᛂ•ᛟᛉ•ᛁᚳᛖᛏᛋᚹᛖᚾᛡᚣᛂᛗ•ᛖᚳᚪ•
	•ᛞᚩ•ᛟᛏᚦᚫ•ᚳᚹᛂ•ᛉᛠ•ᚷᛠᛗ•""",
	
	# p8
	"""ᛉᛁᛉᛗ•ᚢᛉᛗᚳᚦᛈᚩᛒ•ᛡᚾᛏ•ᛠᛉ
	•ᛈᚱᚣ•ᚩᚳᛠᛗᛝᚷᛉᛚᚢ•ᛝᛁᛏᚩ•
	ᛂᚠᛝ•ᛋᛚᚾᛞ•ᚩᛗ•ᛇᚫ•ᚱᛞᚹᛏᛂᚦ•
	ᚣᚦᛋ•ᚫᚣᛖᛋᛉᛟᛒ•ᛠᚱᛇ•ᛈᛝᚢᛈ•ᚩᚦᛉ•ᚪᚻ
	ᛟᚱᛝᚢᛖᚱ•ᚣᛚᛉᛚ•ᛡᛚᚱ•ᛈᚹᛇᚾ•ᛠᚪᚱᛉᛝ•
	ᚣᛋᚻᚢᛚ•ᛋᚣ•ᚷᚾᚢ•ᛇᚫᚾᚾ•ᚩᚫᛖᛞ•ᚪᚩᛂᛡᚢ
	ᚪᛉ•ᚱᛉᛡᛟᛂ•ᛗᛁᛇᛚᛠᚻᚦᛗᛠᚣ•ᚷᛒᚳᛈ
	ᛉᚳ•ᚾᛟᛟᛋᚷᛗᛈᛖᛏᛚᚾᛂ•ᛂᚳᛝᚩ•ᛁᚹᛚᛠᛒ•
	ᚠᚪᛖ•ᛏᛝ•ᚾᛈᛠᚩᛏᚦ•ᚻᛝᛉᛈᚻᛈᚳᛈᚱᚢ•ᛚ
	ᚠᛖᛟ•ᚷᚪᛒᚠᛁᚫᚠᚢᛟ•ᛗᚠᚣᛝᛂᚳ•ᚻᛏᚠᛚᚫ•ᛖ
	ᚦᛋᛚᚩᚢ•ᚫᚩᚪᛗᛟᚢᚹᛇ•ᛒᚾᛋᛚᛝᛂᛟᚾ•ᛗᛚᛒ•
	ᛟᛏ•ᚾᛞᛒᚩᚾᚦᛡᚻᛟ•ᚱᛈᚾᚠᛈᛞ•ᛋᚩᛁᛠᚣᚾ•ᛇ""",
	
	# p9
	"""ᚣᚹᚫᚷᛂ•ᛝᛗᚪᚹᛈ•ᚪᚢᚾ•ᛈᛡᛗᛖᛞᛟ•ᛁ•ᛉ
	ᛡᛗ•ᚠᛈᚩ•ᚦᛉᛞ•ᚩᛞ•ᛋᛈᛉᛡᚷ•ᛟᚻᚠᚦᛉᛂ
	ᛟᛋᚦᚣᚦ•ᛏᚻᛋᚣ•ᚻᛠᚷᛚᚫᚱᛏ•ᚢᛋᛟ•ᚦᚠᚠᚣ
	ᛟᛡ•ᛇᚳᚣᛒᛚᛝ•ᛠᚱᚻᛞ•ᛂᚣᛏᚫ•ᚻᛞᚳᛋ•ᛉ
	ᚠᛞ•ᚦᛗ•ᚳᛇᛝ•ᚫᚾᛡᛠᚹᛁᛡ•ᛒᛗᛝ•ᚷᛈᛁᚳ•ᛠ
	ᛚᚷᛉᚣᚣᚱᛂ•ᛉᛁᛂᚢ•ᛖᚣ•ᚪᛝᛈ•ᛡᚫᚳ•ᛖᛠ
	ᚹᛒᚦᛟᚠᛗ•ᚫᚱᚠᚩᛏ•ᛝᛉᛞ•ᛗᛖᛡ•ᚩᛈᛋ•ᛇᛞ•
	ᛇᛟᚫᚾ•ᚷᛗᚣᛁᚫᛁᛂ•ᛈᛂᚩᛡᚷ•ᛈᚳᛂ•ᛚᛖᛡᚻᛚ
	ᚷᚱᛇ•ᛟᚣ•ᛠᚣᛗᚹᚾᚹ•ᚠᛁᛂᚢᛗᚫᚾᚳᛗᛠᛁ•
	ᚩᛇ•ᛒᛚᛞ•ᚾᚹᚠᚾᛒᚱ•ᛋᛟᚦᛡ•ᚪᛡᛏᚷᚷᚹ•ᚪᛋᛡᚦ
	ᛋᚦᛋᚠᛗᚷᛞᛠ•ᛝᛈᚩᚪᚣᛝᛈᛋ•ᛟᚾᛇᚪᛖ•ᚻᚢ
	ᚷ•ᚩ•ᚢᚦᛏ•ᛒᚷᚣᛝᚠᚣᛁᚻ•ᚹᛡᛠᚱᚫᚹᛡᛞᚪᚦ""",
	
	# p10
	"""ᚳ•ᛉᚢ•ᛈᛏᛋᚢᛖ•ᚷᚦᛡᛚ•ᛖᛋᛠᛝᛉᛈᛉ•ᚾ
	ᛟ•ᛞᛟᛒ•ᚾᚹᚢᛁᛇᛚᛞ•ᛁ•ᚦᚣᚷ•ᛟᛈᛡ•ᛖᚪ•ᚠᛋᛉ
	ᛞ•ᛖᚷᚦᛠ•ᚾᛋ•ᛞᛟᛗᛖ•ᛗᚾᛉ•ᚹᛒᛠᛈᛟ•ᛗ
	ᛉᚫ•ᛂᚩᛞᚻᛡᚷᚠ•ᚣᛗ•ᛁᚷᛉᚻᚹ•ᚾ•ᛋᛗᚷᛠ•
	ᚣᛚᚱᛂᛗᛉᚣ•ᛇᚱᚢᛟ•ᚣᚦᚢᛟᚩ•ᚱᚢᚹ•ᛁᛒᚳ•
	ᛠᛏᛞ•ᛚᛖᛋᛂ•ᚳᛟ•ᚷᛞᛡ•ᚢᚹᛝᚻᚫᚢᛈ•ᛏᛈ
	ᚩᚣ•ᚾᛇᚦᛟᛏᛇᚳᚠ•ᛒᚪᚾ•ᛗᚦᛝ•ᛟᛠᚢᛁᚪ•ᚾᚻᛝ
	ᛉᚩ•ᛇᛁᛡᚠᛟᛒᚦᚠ•ᛋᛒ•ᚠᛞᛇ•ᚩᚦᛏ•7•ᚷ•ᛚᛂᛖᚫ
	•ᚣᛁᚫᚹᚻ•ᚫᛏ•ᛁᛉ•ᛉᚻᛞᚩᛠ•ᚫᛋᛝᛚᛝ•ᛖᚩ
	ᚻᛗᚩᛟᛒᚦ•ᚱᛚᛋ•ᚳᚻ•ᚪᛡᚾᛇᚱᛉᚦ•ᚣᛉᚻ•ᛡᚾ
	ᚢ•ᛗᛉᚹ•ᛖᛈᛖ•ᚩᚳᛈᚳᛞᚪᛉᚢᛗᛝᛟ•ᛋᚾᛟ
	ᛉ•ᚠᚱᚳᛒᚢᛂᚱᚫᛝ•ᛒᛋᛟᛠᛡᚪᛚ•ᛏᛟᚾᚫᛟᚪ•ᛁ•""",
	
	# p11
	"""ᛡᛋᚳᛖ•ᚹᛒ•ᚾᛚᛝ•ᚦᚾᛁᛠ•ᛒᛡᚱᚠᛖᛁᚹ•ᚾᚠᛗᚢ
	ᚷᚾ•ᛂᛚᚳᚱ•ᛝᚣᛉᛋᚪᛟᚱᛉᚳ•ᛒᚫ•ᚠᚢᚪᛖᚪᚹ•
	ᛚᚾ•ᛂᛉ•ᚻᚦᛉ•ᛗᛚᚾᛖ•ᛏᛝᚦᚪᚩᚢᛗᚣ•ᚠᛝᚪ•
	ᚻᛡᛇᛡ•ᛚᛏᛁ•ᛇᛁ•ᚳᚢᚢᛖ•ᚳᛒ•ᚫᛇᚠᚦᚳᛚᚩᛉᛚ
	ᚩᛚ•ᚠᚳᛠ•ᚪᚠᛟᚫᚠ•ᚾᚳ•ᚢᛒᚱ•ᚾᛇᚩᛉ•ᛁᚳᛟ•ᛞ
	ᛉᛠᛝᚠᚱᛡᚳᛇ•ᛉᛟᛈᛗᛞᚳᚦᚹᛈ•ᛡᚻ•ᚾᚦ
	ᛇᛏᚹᛖᚢ•ᚫᛇᚦ•ᛝᛟᛏᚳᚷᛒᛠ•ᚪᚳᛒᚪᚩᚹᚫ•ᛉ
	ᚢ•ᚫᛖᛒ•ᛇᛏᚢᚩ•ᛟᛞᚠᚢᛋ•ᛡᛂᛗᚦᛠᛏᚪ•ᛒ
	ᚹᚣ•ᛏᛂᚻᚦᚫ•ᛚᚪᚱᚫᛟᚦᚩᚾᛟᛁᛖ•ᛡᚠᚷ•ᛋᚠᚦᛏ•
	ᛠᛡᛠᛁᚢᛡᛇᛝᛞ•ᛉᛏᚠᛒᚻᚢᛋᚳᚱᛇᚹ•ᛇᛈ
	ᛋᚢᛚᚪᛈᚢᚳᛖᚠᛞᛉ•ᚦᛠᛇᛝᚻ•ᚣᚱᛗ•ᛟᚾᛚ•
	•ᛈᚹᛞᚱᛂ•ᚪᛝᛞ•ᛁᚦᛏᚷᚢᚹᚳᚻᛖᚩᚪᛖ•ᛉᚪᚢ•""",
	
	# p12
	"""ᚳᛁ•ᚱᚳᚹ•ᛠᛇᛏ•ᚦᚳᚻᚢ•ᛡᚹᛟ•ᚷᛇᛈ•ᚢᛈᚦ•
	ᚷᚣᚢᚪᛗ•ᚹᚳᛖᛝᚱᛠᛞᛏᚻ•ᛂᛁᛈᚻᚠᛉᛝᛈ
	ᚾ•ᛒᚳᚪᚷᛋᛟ•ᛉᛠᛈᚪᚩᚷᚠᚳᛡᛂ•ᛠᚢᚠᛋᛚ•
	ᚣᛚ•ᚢᛒ•ᛉ•ᚱᚣᚾ•ᛁᛠ•ᛚᚹᛋ•ᚠᚦᚪᛠ•ᛈᚷ•ᛏ
	ᚷᛡᛟᛠᛡᛒ•ᛉᛂᛒ•ᛖᚾ•ᛞᚠᛠᛗ•ᚦᚪᛗᚠᚪ•
	ᚻᛡ•ᛗᛁᛏᛟ•ᚻᚣᚹᛏ•ᚠᛒᛁ•ᚫᛖ•ᛝᛒ•ᛚᛏᛠᛉ•ᛟ
	ᛋᚾᛉ•ᚹᛏᛠᛏ•ᛖᚢᛡᛖ•ᛉᚾᛇ•ᛟᚳᚾᚠᚩᚾᚠ•ᚳ
	ᚪ•ᚷᚱᚩ•ᛠᚦᚹᚣ•ᛒᛁ•ᛝᛇᛟ•ᚣ•ᚷᛗᚩ•ᛁᚷᛂ•ᚩᛇ•ᚢ
	ᛁᛉᛝᚪᚱᛉ•ᛏᛂᛞᛈ•ᚾᛝᚷᛏᚢ•ᛚᚷᚳᛏ•ᚢᛒᛇ•
	ᛈᚩᚣᚢᛏ•ᛡᚫᛏᚹᛏᛇ•ᛡᚫᚫ•ᚦᛏᛝ•ᛠᚳᛁᛉ
	ᚻᚦᚣ•ᚻᛚᚾᛋᚱᛡᚫᛚᚫ•ᛖᚷᚻ•ᛞᚾᚻᛠ•ᚠᚪᚹᛖᚠ
	ᛂ•ᛒᛇᚱᚹᛏᛉᚾᛠᛖᛁ•ᚠᚾᛡᚳ•ᛋᛟᚹ•ᛈᚷᛝᛟ•""",
	
	# p13
	"""ᚷᚦᚠᛂᚷᚳ•ᛒᛁᛗᛚᛇᛠᚹ•ᚾᚫᚹᚷ•ᚩᚻᚪᛏᚾᛂ•ᚣ
	ᛝᛏᛡᛝ•ᚢ•ᚩᚠᚣ•ᛗᚢᛒ•ᛏᚠᛈ•ᚱᚩ•ᛉᚩᛝᛒ•ᛖ
	ᛏᚩᛉ•ᚣᛗᚠᛉ•ᛖᚩᚫᚷᚣᛚ•ᚩᛇ•ᚠᛋᚫᛇᛗ•ᛡᛟᚹ
	ᚾᚩᚢᚹᛖᛁ•ᚾᚦᚫᛠᚪ•ᛠᛚ•ᚹ•ᛡᚩ•ᚢᚦᛗ•ᛝᛚᚪᚠ
	ᛝ•ᛚᚠᛚᚳᛒᚢᛝᛉ•ᚣᛡᚪᚷ•ᚹᛟᚪᚻᚹᚢ•ᛖᛠᚷ•
	ᛁᚪᛏᛂᛗ•ᛏᛖᛁ•ᚣᛡ•ᚦᚾᚠᚦ•ᚩᛈᚻᚪ•ᚻᛋᛠ•ᛡᛉ
	ᚪᚫ•ᚠᚣᛞᛠᛇᚠᚫ•ᛏᛗ•ᚳᛡᚷ•ᚱᚢᛞ•ᛂ•ᛋᛡᛇᚩ
	•ᛚᛟ•ᚦᚱᚫᛒᛚᚦ•ᛖᚪᚦᛗᛚ•ᚦᛉᚪᚱ•ᛟᛖᛒᛂᚱᛂᛖᛁ
	ᛈ•ᚪᛖᛠᚠᛂᚢ•ᛞᚹᚦᚣ•ᛉᚷᚩᚳᛡ•ᛇᛗᛞᚳᛏ•
	ᚻᛚᚦᛝᛖᛗᚱ•ᛒᚷᛞᛉᛗᛒᛉᚳᛝᚦᚣᛞᚫᛠ•ᛋ
	ᛏᛗᛏᚻᚹ•ᛇᚳᚪᛞ•ᛠᚢᛒᛉ•ᛡᛁᛡᛚ•ᚷᛋᚦᛞ•ᚠ
	ᚢᚩᛠ•ᛚᛋᚣᛏ•ᛋᚪᛞᚫᚹᛂᛞ•ᛋᛈᛋᛂ•ᚪᛖᛁᛇᛒᛟ""",
	
	# p14
	"""•ᛏᛂ•ᚠᚩᛚᛞ•ᚾᚷᚳ•ᛚᚷᛗ•ᛠᚦᚢ•ᛟᚻᚾᛟᚣᛡ•
	ᛇᚻᚣᚪᛈ•ᚾᛋ•ᛞᚫᛠᚳᛉᛂ•ᚦᚹᛋᚱᚦᚫᚾ•ᛡᛚᚣ
	ᚫᛋᛖ•ᛟᚣᛝᛡ•ᚦᚣᚷᛇᚱ•ᛋᛠᛏ•ᛡᚳᛉ•ᛠᚷ•
	ᚳᛒᛋ•ᚹᚾᚻᛖᛝᛋ•ᚩᛡᛗᛉᛝ•ᛉᚦ•ᛠᛞᚳᛒᚷ
	ᛉᚹᛝᚢ•ᛉᛞᛈ•ᛉᛡᛈᛟ•ᚾᛡᚠᛡᚢᛋ•ᛉᚪᛖ
	ᚻᚱᚣᛠᛇ•ᛒᛟ•ᚪᛝᛡ•ᚳᚱᚳᛈᚩᛏ•ᚻᚣᚫᛁᛋᚩᚦᛚ
	•ᛟᛚ•ᛋᚪᚢᚪᛈᚻ•""",
	
	# p15
	"""        •ᚠᚢᛚᛗ•ᚪᛠᚣᛟᚪ•
	3258    3222    3152    3038
	3278    3299    3298    2838
	3288    3294    3296    2472
	4516    1206     708     1820
	ᛚᚢᛝᚾ•ᚳᚢ•ᛒᚾᛏᚠᛝ•ᛁᚢᛁᚢ•ᛟᚫᛂᚠᚫ•ᚢ
	ᚷᛉᛇᛈᛉ•ᚣᛠᛚᚪᛉ•ᛟᛉᛡᚦᚻᛠ•ᚾ
	ᚪᚳ•ᚢᚷᚾ•ᛈᛖᚾᚦᚩᚢᛁᛡᚱ•ᛏᛁᛒᛇᚳᚠᚷ•ᚩ
	ᚦᚪ•ᛁᛈᚻᛡᛒ•ᚹᛈᚻᚱᛞᛉᛏᚢ•ᚣᛒ•ᚠᛋᛉᚢ•ᛗᛁ•
	ᛡᚱ•ᛝᚢᚠᚦᛝ•ᛈᛟᛒ•ᚻᚷᚻᛡᛚ•ᚩᛞᚪᚳ•ᚦᛈᛞᛋ
	ᛡᚻᛇᛚ•ᚢᛏᛋᛞ•ᚦᚢᛞᛝ•ᛚᛉᛝ•ᛏᚩᛚ•ᚪᛚ•ᚣ•ᛟ
	ᛡᛉᚣ•ᛒᚻᚫᛂᛡᛁ•ᚱᚦᛚᚠ•ᛠᚾᛝ•ᛉᛗᛒᚩᛠᛈ•""",
	
	# p16
	"""ᛖᛞᚪᚫᛏᚩᛠᛖᛠᛉᚳᛠᛏ•ᚩᛞᚳᛠᚾᚳᚦ
	ᛗ•ᛞ•ᚷᛁᚳᚹᛟ•ᚪᚢᛒᚳᚫ•ᚦᚱ•ᛋᚣᚪ•ᛏᚦᛒ•ᛝᚹᛋᚱᛁ
	ᛝ•ᛒᛁᚪᚫᛚ•ᛏᚱᛡᚫᚠᛞ•ᛝᛂᚩ•ᛡᛠᛉ•ᚪᛡᚻ•ᚱᛒ
	ᛁ•ᛞᛡᛂᚪᛈᚱᛋ•ᚢᛡ•ᚻᚷ•ᛚᛟᚠ•ᚻᚷᚫᛋ•ᛈᚹᚷᚷ
	•ᛗᛟᚪᚾᚱ•ᚩᛟᛞ•ᚷᛟᚠᛠ•ᛡᚷᚳ•ᛉᛠᚠᛚ•ᛒᚫ
	ᛈ•ᚩᛂᛈ•ᛂᛗᛠ•ᚾ•ᛉᚪ•ᛡᛖᛋᚷᚫᚦ•ᛂᚷᛉᚩᚦ
	ᛂᚳᚣ•ᚢᛂᚦᛂᚪᚾᛏᛒ•ᚳᛈᛡᛂᛋᚫ•ᛋᛗ•ᚻᛞᛠ
	ᛉᚢᛗ•ᛏᛠᛖᚣᚠ•ᛂᛏᛋᛗᛞᛟᛁᛝᚪᛉᛖᛈ•ᛚ
	ᛇᛞᚦ•ᚪᛋᛉ•ᚳᛒᚢᛟᚳᛒᛚᚾᛟᛝᛉᚩ•ᛖᚳ•ᛝᛟ
	ᚳᛁᛒᛈᚫ•ᚣᛖᛂᛝ•ᛞᚢᚱ•ᛉᛟᚩ•ᚠᚹᚩ•ᚣᛁᚠᚢᛇ•ᛚ
	ᛏᛈᛒᛗ•ᛇᛝ•ᚢᚳᚱᛡ•ᛖᚩᛁᚣᛂᛏᛡ•ᛖᚠᛇᚠᛚ•ᛁ
	•ᚣᚷᚠᛝᛡᛈᚷᛒ•ᛡᚩᚷᛡ•ᛟᚾᚹᛡᛈᛟ•ᚦᛈ•ᛟᚷ""",
	
	# p17
	"""ᛚᚦ•ᛈᛞ•ᚦᛇᛒ•ᛡᚪᛒᚪ•ᚾᛗ•ᚳᚾᛖᛡᚹᛝᛏᚱ•ᛝᚫ
	ᛚᛟᛁᛇᚣ•ᛝᛡᚾᛏ•ᚱᛁ•ᛋᚪᛖ•ᛇᚢ•ᛝᛞᛂ•ᚠᚱᛠᛗ
	ᛠᚪ•ᚫᛈ•ᛏᚠ•ᛖᛏᚷᚾᚠᛁᚠ•ᚱᚻᚱᛇᛒ•ᚻᛈᛏ•ᛇᚱ
	ᛝᛡᛒᚹᛚᛏ•ᛗᛉᚦ•ᚾᛂᚳᚫ•ᚷᛈ•ᛋᛖᚩ•ᚢᛝᚩ•ᛏ
	ᛈᛁᚣᚾᚪ•ᛏᚹ•ᚠᛗᚾᛟᚾᚳᛒ•ᛂᛉᛡ•ᛟᚪᛁᚫᛝ•ᛒ•
	ᛉᛏᛂᛁᛋ•ᛠ•ᚳᛖᚱᚦᚣᚩᚣ•ᛈᚫᚷ•ᛡᛂᛁᚩi •ᚱᚦ
	ᛠ•ᛇᚦᚩᛉ•ᚾᚱᚾᚫᛁᛉ•ᛁ•ᛝᚣᚫᛡᚫᛗ•ᚹᛖ•ᛇᚷᚻ
	ᛖᛗ•ᚷᚢᛞᚹ•ᛂᚻ•ᛉᚱᚢᛂᚢᚾᛈ•ᛋᚣᛂᚫ•ᛈᚳ
	ᚣᚳᛒᛡ•ᚫᛟᚪᚠ•ᛏ•ᚷᚩᛇᛟ•ᛁᚱᛗ•ᛖᛉᛟ•ᛗᛇᚫᛟ
	ᚦ•ᚱ•ᛞᛁᚢᚦᚻᛗᛡᚾ•ᛁᚦᚻᛚ•ᛏᚳ•ᚪᚦ•ᚠᚪᚫᚣᚻ
	ᛠ•ᚦᚠᛋᚠᛝᚷᚱᛈ•ᛏᛂᛉᛟ•ᚷᛚᚻ•ᚩᚪᚦᛏᚳᛁ•ᚠ
	ᚣᚢᛁᚹ•ᛟᚪᚣᛁᛠᛂᚪ•ᛟᛝᚦ•ᛟᚠᚦᚾ•ᛇᚷ•ᛠᛚᛒᚠ""",
	
	# p18
	"""•ᛠᚪᛂᛇᛠᛚ•ᚱᚷᛋ•ᚹᚩᛒᛁ•ᛠᚳ•ᛁᛞᛂ•ᛖᛗᚱ•ᚷ
	ᚪᚻᛠᛚᚷᚩ•ᛉᚻ•ᛡᛝ•ᛞᚱᚹᚩᛈᛡ•ᚣᚳᚦ•ᛁᛇᚢᛁ•
	ᛟᚦᚠᚳᚻ•ᚩᛁ•ᛝᚾᛁᛞ•ᛏ•ᚫᚱᛝᚫᛈ•ᛠᛞᛇᛉᚳ
	ᛠᚩᛟᛖ•ᛗᛈᛒᚦᛝᛋᚢᛡ•ᚻᛡᛏ•ᛉᛇᚷᚠᛡᛡ
	ᛟᚢ•ᛡᚦᚣᛞᚪᚫᛝᛒ•ᚳᚩᚷ•ᛏᛞᚦᛁ•ᚠᛒᛖ•ᚦᛟᚳ•
	ᚠᚻ•ᛞᚠᚣᛋᚾᛟ•ᛠᛇᛂ•ᛖᛉ•ᚩᛈᛠᛚᚪ•ᛟᚩᚾ•
	ᛂᛉᛋ•ᚣᚫᚷᛖᚩᛟᚢᚱᚹᚢ•ᛟᛡᛂᛇᚢᛞᛉ•ᛒᛇ
	ᚳ•ᛝᛚᛗᛠᛗ•ᚪᚱᛡᛗᛒᚩᚹ•ᛋᛖᚾᚻᚣ•ᛈ•ᛞᛚᛞ
	•ᛈᛏ•ᚪᛞᛚᛉ•ᛟᚱᚾᚹ•ᛠᚠᛁ•ᛟᚾᛒ•ᛇᛟᛖᛝᚳᚠ
	ᛏᛞᛏ•ᛇᚫ•ᛝᚢ•ᛠᛡᚫᛖᛟᛞᛝᛠ•ᚠᛗᛒᛚ•ᛏ
	ᚢ•ᛈᚱᚹᛟᛇᛉ•ᚳᛟᛈᛏ•ᚢᚠᚳᛞ•ᛂᛋᛞᛈᛚ•ᚠᛝ
	ᚱᛂᚣ•ᛞᛗᛖᚣ•ᚢᛖᛝᛠᚳᛞᛈᚩᛠ•ᛏᛒᚳ•ᚷ""",
	
	# p19
	"""ᚾᚩᛟᚾᚠ•ᚩᛁᚠᚢᛋᚾ•ᛞᚹᛠᛇᛈ•ᚱᚩᚩᛂ•ᚪᛟ•ᛇᛠ
	ᛂᛁ•ᛟᛂᛞᚢᚳᛝᚩ•ᚱᛝᛋ•ᛂᛁᛈᛉᛖ•ᛞᛁᚾᛗᛗᚳ
	•ᛉᚩᛁᛂᛞᚳ•ᚢᚪᛇ•ᚦᛡᛇᚻᛠᚣ•ᛠᚻ•ᚠᚩ•ᛡ
	ᛠᛋᛟᚪ•ᚹ•ᚫᚻᚩᛂᚢᚱᚩᚣ•ᛏᚫᚷ•ᛂᛚᛂ•ᛝᛏ
	ᛖᛒᛚᛉᚻ•ᚱᚩᚫᛇᛈᛂᛠ•ᚳᛈᛚᚣᛈ•ᚪᛠᚻᚻᛋ
	ᚫ•ᚩᛝᚹ•ᛋᛞᚠᚳᛠ•ᚩᛇᚫᚪᚩᚹᛗᚪ•ᚣᚫᚷᚫᛂᚱᚹ
	ᛞ•ᚱ•ᚦᚷᚳᚹ•ᚾᚷᛡ•ᛚᛒᚳ•ᛂᚷᚹᚹ•ᚱᛁᚠᛏ•ᚠᛚ•ᛋᛂ
	ᛚᚪᛂᚱᛏ•ᛞᚷᚫᛠᚠᛉᛞ•ᚫᚷᚻᛏ•ᛗᚣᛈ•ᛏᛒᛟ
	ᛝ•ᛂᛋᚾ•ᛝᛁᚹ•ᚦ•ᛠᛝᛞᚾᛟᚷᚫ•ᛁᛗ•ᛝᛉᚱᛞᛋ
	ᛗ•ᚠᚫᚹ•ᛟᛋ•ᚦᛞᛞᛈᛝ•ᛞᛡᚷᛒ•ᚪᛟ•ᚦᛡᛒ•ᚪᚹ•
	ᚾᛉᚫ•ᛚᛈᛁ•ᛒ•ᚠᚾᚠ•ᛡᚩᛏᛞᚾᛋᛖᚳᚻ•ᛖᚻ•ᚢᛟ•
	ᚪᛖᛗᛝ•ᛠᚫ•ᛈᚩᚪᛞ•ᚠᚫᚻ•ᚠᛏᚦᛂᛚᛂᛒ•ᛗᛇ""",
	
	# p20
	"""ᛈ•ᛂᚢᛒ•ᚷᛁᛇ•ᛈᛉᚣ•ᛈᛟᚦᛞᚱᛠᚪᛡ•ᛝᛡᛒᛚ
	ᚻᚦᚫᛉ•ᛟᚫ•ᚪᛇ•ᛉᚳ•ᛠᚠᚫ•ᚢᚣᚦᛋ•ᚠᛝᚠᚱᚹ•
	ᛟᛒᛗᚷᛞᚾᛡ•ᛞᚪ•ᚻᚣᛇ•ᚱᛚ•ᛖᚣᛇᚻᛠᚩ•ᚢ
	ᚳᚱᚻ•ᛡᛟᛗᛠᛝᛂᚦ•ᛂᚢᛁᛇ•ᛂᛁ•ᛖᚷᛁ•ᚪᛇᛏ•ᛝ
	ᛡᚳᛚ•ᛇᚠᛗᚪ•ᚷᛚᛒᛋ•ᛉᛞᚫᛟᛋᛚ•ᚹᛏᛠᛗ•ᛚᚦ
	ᛗ•ᛝᚦ•ᚣᛈᚠ•ᚪᛞᛚᚪᛖᛚᚩ•ᚱᚷ•ᛚᚳᛇᛏᚷᚣᛟᛗ•
	•ᚪᛁ•ᚷᛂᛒᛡᛗ•ᛞᛈᚪᚳᛠᚷᛋ•ᛏᛈ•ᚩᛋᛏᛗᚱᚣ
	ᛋᛉ•ᛁᛂᛚᛝᛚᛁ•ᛉᚢᛠᛗᛇᚢᛋᚻ•ᚳᛉᛂᚩ•ᚠᛂᚠ•
	ᛁᚣᛁᛟ•ᛏᚷᚱᚦ•ᛡᛒᛋᚳ•ᛇᚢᚷ•ᛚᚱ•ᛁᛗᚱ•ᛗᛝᚻᛈ
	ᚫ•ᛝᛋᚫ•ᛖᛈᛁ•ᛒᛇᚹᚫᚢᛂᚳᛒ•ᚦᛋᚹᚦᚫ•ᛡᛟᚷᛚ•
	ᛞᛚᚢᛟᛡ•ᚱᛞᚱᛒᛂᚳᚢᛠ•ᚩᛉᛉ•ᛝᛡᛂ•ᛁᚫᛟ
	•ᛖᛗᚹ•ᛖᛉᚦᛗᚪᛋᛉ•ᛞᚦ•ᛡᚢ•ᛉᛗᚫᛋᚳᛖ•""",
	
	# p21
	"""ᚳᚫᛠ•ᛞᚳᚷ•ᚩᛁᛇ•ᚾᛟᚷᚣᚳᚦᚳᚦ•ᛗᚣ•ᛈᚪᛒ
	ᛈ•ᚻᚢᚻᚾᛏᚫᛒᛇᚩᛁᛈ•ᚫᚩ'ᚣ•ᛡᚣᛗᚷ•ᚠᚱᛡᛚ
	ᛏ•ᛖᛟᚩᛈᛚᚩᚷᛁᛟᛠ•ᛞᛖᚳᛗᛁᚣ•ᛈᛚ•ᛁᚹᛋᛂᚹ•
	ᛟᛡᚪ•ᚦᛖᚩᛂᚷᛋᛝᚣᛗᛟᚻ•ᛗᚠᚦᛉᚦᚫᛋᛈᚣᚩ
	ᚠ•ᛈᛟᛋᛖᚫᛇᛗᛚᛈᚾ•ᛡᚠᚳᚾᚩᛂᛋᛡ•ᚫᛂᚦᚪᛠ
	•ᛈᚻᛋᛟ•ᛗᚹ•ᚱᚣᛁᚢ•ᛉᚹᛋᚱ•ᛞᛈᚦᛈᚩ•ᛞᛂᚩ•
	ᚢᛈᛖᚪᚫᛉᚫ•ᛏᚱᛟᛏᛒ•ᛠ•ᚫᚳᚾ•ᛖᛝᚦᛂᛂᚠ
	ᛚᚾᚩᛒ•ᛉᚷ•ᚪᚩᛚ•ᚪᚢ•ᛞᚻᚳᚹᛚᛡᛞᛇ•ᛟᚩᛡᛚᚳ
	•ᛡᚳᛉ•ᛝᛠᛝᚷᛝᛞᛂᛏ•ᛠᛈ•ᚹᛈᛗ•ᛈᚱ•ᚫ
	ᛏᛖᚢᛝᚫᛡ•ᚾᛁᛠᚻᚦᚣᛠ•ᚫ•ᚩᛉᛋᚩ•ᛂᚠᛏᚷ•
	ᚹᛁᚪᛁᚩᛁ•ᛝᛠ•ᚾ•ᚷᛗᚹᚦᛖ•ᚷᛟᚪᚹᛞᚻᚢ•ᛡᚹ•
	ᚣᚷᛉᛒᚪᚾᛝᛡᛂᛡ•ᚠᚷᛈᚦᚠᚦ•ᛁᛈᚪᛝᛋᛞᛟᚩ""",
	
	# p22
	"""ᛝᛗ•ᛁᚷ•ᛂᚷ•ᚳᚩᚦᛖᚦᛂ•ᚣᚠ•ᚦᚳᛂᛡᛖᚢ•ᛉᛂ
	ᚳᚻᛂᚱᛂ•ᚪᚻᚾᚦ•ᛚᚷ•ᚱᚦ•ᛒᚪᚩᛖᚢᛡᛂᚹᛏᚱᚹ
	ᛟ•ᚦᚳᛗᚦᚠᚫᚻ•ᛡᚠᛠᚣᚪᚦᛚᛏᛒᚢᛝ•ᛖᛋᛗᚱ•
	ᚪᚹᛒ•ᚹᛒᛗᚱᚾᛗᚻᛗᛁᚾᚪᛞ•"ᛡᛖᚩ•ᚾᚹᛡ•ᚢᛂ
	ᚦᛠ•ᛚᚳᚷᛚᛇ•ᛟᛠᛠᚪ"•ᛇᛉᚣᚪ•ᚷᛏᚩ•ᛖ
	ᚹᛒᛈᚷᛝᛒ•ᛡᚦᚠᛋᚾ•ᛒᚦᚠ•ᛇᛝᛠ•ᚠᚾᛉ•""",
	
	# p23
	"""ᚢᚪ•ᚹᛝᚷᛉᛞᚷ•ᛁᛒᛁ•ᛇᛏᛒᛁᚣ•ᛠᚷᛋᚫ
	ᛈᚹᛗᛠ•ᛇᛂᛇ•ᚹᚻᛁ•ᚷᛠᛒᚢᚣᚻᚣ•
	ᛝᚹᚢᚱᛋ•ᚩᛡᚠᛡᛠ•ᛞᛟᚦᛗᚳᚾᛉ•
	ᛞᚦᛖᚱᛇᚳ•ᚪᛂᛋᛟ•ᚢᚹᚱᛏ•ᛋᛖᛋᛏ•ᚣᚱᛠᚫᚾ
	ᛞ•ᛈᛒᛡᛋᚢᛞᛖᚣᚦ•ᛚᚹᛟᛋ•ᚷᛚᛂ•ᚫᛖᚩᚳᚦᚹ
	ᛗ•ᚢᚩᚷ•ᚠᚪᚩᛡᛝᛒᛠᚦᚳᚪ•ᚱᛡᛏ•ᛟᚹᚠᚣᛝᚢ
	ᚣᛁ•ᛚᛏᚫᚫ•ᚪ•ᚱᛈᚠᛗᚹᚩᛞ•ᛠᛒᛈ•ᛝᛟ•ᚾᚷᛗ•
	ᛡᛖᚩ•ᚾᛚᛉᛝ•ᛁᛡᚫᛗ•ᚻᛖᚹᛗ•ᛝᛈᛇᛗᛡᛂ•ᚫ
	ᚩᛡ•ᚠᚣᛉᛟᚫᚦ•ᚫᛒᚩ•ᚪᚦᛂᚱᛂᚾᚦ•ᛡᚠᚪᛏnᚾᚻ•ᚷ
	ᚢ•ᛞ•ᚳᚦᚢᚱᚢᛟ•ᛞᚻᚱ•ᚷᚹᛏᛈᛖᚠ•ᚪᚻᛠᚦ""",
	
	# p24
	"""ᛞᚱᚠ•ᛖᛂᚫ•ᚾᚳᚻᚹ•ᛇᛡᛈᛠᚹ•ᛗᛚ•ᚹᛟᚹᛠ•ᚪ
	ᚾᚪ•ᚳᚪ•ᚷᛚᚦᛒᚩᚹᚢ•ᚷᛚᚠᛋᚻ•ᚾᛉᛝᛗ•ᛖᚦᚢᛝ
	ᛡ•ᛈᚣᚢ•ᛉᚷᚷ•ᚹᛞᛁᛋ•ᚦᛡᛡᛈᚳᚪᚩ•ᚢᛗᚢ
	ᛉᚩᚣᚻᛏ•ᚩᚫᛗᚢ•ᚩᚾᛏᛠᛒᛟᛒᚠᛁᛈ•ᛚᛋᛝᚫᚳ
	•ᚫᛟᛏ•ᚢᚩᛉᚾᛡᛋᚠᛖ•ᛉᚱ•ᛗᚩᚩᚫ•ᚠᚢᚦᛖᛞᚾ
	ᚣ•ᛡᛋ•ᛋᚱᛚᛟ•ᚢᚻ•ᚢᚾᛈ•ᛁᚻ•ᛖᛉ•ᚦᛞᛗ•ᛈᛟ
	ᚠ•ᛈᚠᛝᚫᛝᛋ•ᛟᛂᚹ•ᛠᛒᚣ•ᛟᚹᛞ•ᚠᚣᛂᛁᛏᛉ
	ᛚ•ᚩᚦᛝ•ᚠᚪᛋᛡᛁᚻᛒᚱ•ᚪᚢᚣ•ᚫᚢ•ᛟᛠᚪᚣ•ᛖᛟ
	ᚫ•ᛖᛈᚠᛒ•ᛈᛂᛁ•ᛋᛝᛒ•ᚱᚦᚳᛇ•ᛚᛁᚢᛈᛏᚳᛒᛉ•
	ᛖᚪᚣᚠᛗᚳᚣᚱ•ᚻᚹᛏᚾᛡᛉᚫᚦᛟ•ᚳᚹ•ᛠᚠ•ᛏ
	ᛠ•ᛝᚩᚻ•ᛡᛠᛒᛋᚻᛟ•ᚫᛁ•ᛠᛏᛁᛋ•ᛏᚫᚻᚱ•ᚻᛂ
	ᛋᛡᚹᚾᚾᛡᚹᛚ•ᚢᛖ•ᛏ•ᚱᛝᚳᚣ•ᚪᛉᛇᛝᛋᛖᛇᛁ""",
	
	# p25
	"""ᚻᚾ•ᚷ•ᚹᛉᚳᛉᚣ•ᛋᛈᚳᛟᚱ•ᛒᚣᛂᛝᛖᛁ•ᚾᚷᚪ•
	ᚣᚷ•ᛚᛒ•ᚢᛂᚩ•ᛝᛉᛉᚪᛖ•ᛒᚦᛉᛡᚱ•ᛏᚷᚹᛂᛋ
	ᛁᚠ•ᛠᛁᛡᚦᛝᚾᛖᚾᚠᚩᛗᛖᚣᚪ•ᚳᛖᚳᚹᚪᚫᚹ•ᛇ
	ᚢᚦᚻᛉᚢᚾ•ᛠᛚᚢᚾᚦᛈᛋᚢᛈᚱ•ᛞᚫᛟᚱᛡᚫᚪ
	ᚢ•ᚢᛗᛚᚦᛠ•ᛚᛝᛈᚣ•ᚩᛋᛟᚪᚱᛗᚦᛟᛈ•ᛚᛋ•ᛏᛁ
	ᚠᛋᛖᚹᛝ•ᛗᛞᚩ•ᛠᚫᛡᛒᛏᚩᛋ•ᛖᛏᚪᚠ•ᚫᛒ•ᛚᚾ•
	ᛋᚪᛉᛟ•ᚾᛚᚹᛖ•ᚩᛚᛁᛂᛏ•ᛒᚪᚠᛉᛏ•ᚩᛟᛂ•ᚾᚷᛋ•
	ᚷᛚᚷᛠ•ᛒᚷᛖᚩᚪᚩᛖᛞ•ᚷᛇᛗ•ᚳᚱᚷ•ᛈᛞᚩᚠᚹ
	ᛇ•ᛠᛞᚣᛝ•ᚾᛁᚠᛈᛚ•ᛖᛟ•ᚢᚳᛗ•ᛚᚫᛏᛉᛂᚱ
	ᛉ•ᛁᛠᚷᛚ•ᚷᚳᛋᚩᛝ•ᚫᚦ•ᛗᚻᛟᚠ•ᚱᛋᚳᚦ•ᚣᚩ•ᛒᛁ
	ᚫᚻᛖᚢᛏᛚᛚ•ᛇᚷᛟᚣ•ᛒᚾᚦᚻ•ᛠᛖᛂᛒᚾᛁᛚᛠ
	ᚱ•ᛂᚠᚳᛋᛝᚳᛈ•ᚷᚻᛋᛗ•ᛇᛞᛇ•ᚣ•ᛡᛖᛏᛠᚢ""",
	
	# p26
	"""ᛡ•ᚩᚾᛠᚩ•ᛂᚣᛇᛉᛠᚪᛡ•ᚾᛞᛝᚻ•ᛈᛠᚻᛡ
	ᚢ•ᛝᚻᚦᛈ•ᛉᚢ•ᛠᚣᛈᛟᚦᛋᚣᛈ•ᚠᛏ•ᛒᛁᛟᚪᚷ
	ᛚ•ᛠᚻ•ᛝᛁᛡᛚᛝᚾᛞᚪᛈᚷ•ᚾᛏᚦᛋᛒ•ᛋᛋᛠ•ᚷᚳ
	•ᛠᛗᚢ•ᛖᛉᛒᚷᚫᚠᚩᛁᛉ•ᚠᚪ•ᛠᚱᛇ•ᚩᛁᛞᛋᛚ
	ᚦᛖᛒᛇ•ᛟᚷᚣᚷᚾᚷ•ᚦᚠᚳᛗ•ᚩᛖᛖ•ᚩᚠᛒᚻᛝ•ᚳᛁ
	ᛂᚪᚾᚩᚪ•ᛈᚻᚱᛗ•ᚱᛗᛟ•ᚦᚷᛂ•ᛒᚱᚦᚪᛠ•ᛉᛖᛡ
	ᛞᚦ•ᚱᛝᛂᛒ•ᚾᛏᚣ•ᛏᛋᛒᚾᚫ•ᚢᛖᛁᚩᛡ•ᛂᛇᚢᚦᛚ
	ᚳᛖ•ᛚᛁ•ᛒᚢᚠᚪᚱᛠ•ᛗᛒ•ᛞᛉᛗ•ᚢᛠᛏᚣ•ᚪᛂ
	ᛈᚢᛈᛠᚣᚷ•ᛗᛡᛗᚢᚪᛗᛝ•ᚣᛡ•ᚪᛖᛏ•ᛖ
	ᛋᚪᛟ•ᚳᚻᛁᛋᚠᛁᚾ•ᛈᛟᛝ•ᛇᚦᚣᛏᚫᛉ•ᛖᛟᛏ•ᛞᛡ
	ᛚᛖᛈᛏᚪ•ᛏᚠᚱᚾ•ᚪᛠᚱ•ᛠᚳ•ᚾᚻᚹᛒᛇᛋ•ᛁᚻᚣ
	ᛋᚹᚩᛉᚹ•ᚩᛝᚢ•ᚻᛝᛟ•ᛏᛚᚠ•ᛂᚷᛏᛂᛝ•""",
	
	# p27
	"""ᛗᛈᚣ•ᛚᛋᚩᚪᚫᚻᛚᛖᛇᛁᛗᛚ•ᛚᛋᚳᛈ•ᚾ
	ᚻᚷᚢᛡᚻᚢ•ᛒᚠ•ᛞᛂᚢ•ᛒᛖᛁ•ᚫᚠ•ᛈ•
	ᚫᛈᚦ•ᚱᛗᛚᚳ•ᛒᚷᚣᛗᛠᛒᚫ•ᚾᚦ•ᛗᚠ
	ᛡᛠᚳᛒᚷᚫᚠ•ᛖᛂᚱᚩ•ᛈᛒ•ᚠᛒᚩ•ᛇᚱᛠᚱ•ᛠᚷ
	ᛖᛚ•ᛇᚱᚾᛋᚩᚩᚳᚪᛖᚣᛖᛖ•ᛏᚱ•ᚢᚣ•ᛟᛂᛉ•
	ᛠᚷᛝ•ᚣᛏᛝᚾ•ᚪᛏᛋ•ᛝᚪᛂ•ᚠᛚᛋᚢ•ᚹᛠᛈᛁᛏ•
	ᛁᚾ•ᚱᚱᛝᛗ•ᚣᛗᚠᛁᚫᛁᚪ•ᚢᛟᛒᚹ•ᛗᛁᚻᚣᚹᛞᛚ•ᛟ
	ᛏᛞ•ᛟᚳᛒ•ᛡᛒ•ᚪᛏ•ᚹᛏᛈ•ᚹᛠᚩᚱᚩᛖ•ᚣᛚᛋ•
	ᚢᛡᚱᚠᛂᛇᚱᛡᚦᛖᚢᛏ•ᛝᚫ•ᚾᚪᛠᚩᚪᚾᚪᚦᚷᚩ•
	ᚫᛉᛒᛏᛖᛠᛗᚷᚱᛗ•ᚣᛝᚠᛒ•ᛞᛟᛞᚪ•ᛠᚱᚳᛁ
	ᛈᛞᚠᛗᛝᚻ•ᛋᚩ•ᛞᛈᛉᚾ•ᛟᚱᛡᚾᚳᚳᛏ•ᚾᛈᚠ""",
	
	# p28
	"""ᛈᚳ•ᛂᚦᛒᛁᚹ•ᛞᚹᛝᛠᛡᚹᛚ•ᚹᛂᚾᚪᛟ•ᛏᛞᛉᚣ
	ᛖᚱᛞ•ᚱᛏᛇᛁᚳᛈ•ᛝ•ᚦᛟᚷᛂᚦ•ᚣᛋ•ᛠᚻ•ᚠᛒᛚ•ᛁ
	ᚫᛚᛞᛉᚪ•ᛁᚹᚷ•ᛒᚩᚹᚾᛠ•ᛋᛖᛗᛒᛋ•ᚳᚹᚦᛟᚠᚻᚫ
	•ᛞᚢᛁᛒᛞ•ᛇᛝᛈᚠᛁ•ᛟᚢᚣᛏ•ᚻᚱᛖᚾᚳᛈᛡᛈᛞ
	ᛂ•ᛁᛏᛗᛋᚫᛉᚩᚣ•ᚪᛂᛗᛡᛖ•ᛇᛂᚠᛗᚱ•ᛞᛟᚪᛒ
	ᛞᚻ•ᚾᛈᚪ•ᛇᚱᚻᚾᛝᛠᚠᚾᚠ•ᚩᛗᛋᚾ•ᛠᚪᛁᚢᛚ•
	ᚪᚫ•ᛂᛉᛡᚠ•ᛁᛖᛈᛠᚻ•ᚠᛇᚩᚹ•ᛠᛂᛇᛁᛠᚫ•ᛂ
	ᛒ•ᛋ•ᚠᛖᚷ•ᛋᛁ•ᛟᛗᛒᛁᛝᛏᚪᚢᛁᚦ•ᚩᛝᛗᚠ•ᚹᛟᛒᛟ
	ᛡ•ᚠᚣᛝᚩᛠ•ᚳᛚᛈᚱ•ᛞᛂᚩᛝᛂ•ᚪᛖᛗᛈᚾ•ᚠ
	ᛠᚷᛞᛒ•ᚩᛉᚷᚾᚣᚷ•ᛠᛈᛂᛞᚾᛟᚩᚢᚾᚹᛗ•
	ᛂ•ᚢᚷᛠ•ᛗ•ᛇᚪ•ᚻᚦᛡ•ᛝᛈᛞᛒ•ᚳᛉᚳ•ᛠ
	ᛉ•ᛟᚣ•ᛒᚦᛁᛂᛚᛡᛝᛡ•ᚹᛂᚫ•ᛋᛗᚪᛡᛠᛇᛝᛏ•""",
	
	# p29
	"""ᚦᛞᚷ•ᚢᛏᛚᛏᚣ•ᚢᛝ•ᚷᛟᚪᛏ•ᛂᚦᚣ•ᚫᚻᚪ•ᛒᛝ•
	ᚦᚢᚱᚪᚾᛞ•ᛁᛝᚫ•ᛚᚫᚷ•ᚹᛁᛒᚣ•ᚾᚫᚠ•ᛚᛋᛒ•ᛈᛟᚪᛟ
	ᛞᚷᛟᚣᛉᚷᛚ•ᛋᛠᛁ•ᚳᛟᛁᚦᛈᚹᛉ•ᛖᚢ•ᛟᛂᛝ
	ᛋᚢᛝ•ᚳᛡᛠ•ᛚᛇ•ᛚᚷᚢᛁᛏᛒᛋ•ᛞᛁ•ᚠᚠᚷᚠ•ᚦᛂ
	ᚳ•ᚫᛟ•ᛁᛗᛡᛁᛇᚦ•ᚩ•ᚢᛈᛒ•ᚻᛋ•ᛂᚣᛂᛖ•ᛒᛇᛇᚱ•
	ᚹᛂᛏᛡ•ᚳᚪᚫ•ᚩᛈᚱ•ᛡᚾᛗᛁᛝ•ᚻᚹᚦ•ᛡᚦᚻᚦ•ᛉ
	ᚫᚫᛋᚳᛡᚾᛇ•ᛟᛉᚢ•ᚱᛂᛖ•ᛚᚾᛞ•ᛗ•ᛏᚱᛟᚦ•ᛁᛝ
	ᛡᛒ•ᚳᚩᚹᛟ•ᛏᛗᛋᚱᚷ•ᚱᛚᛞᛚ•ᚩᚣ•ᛞᚳᚪᛖᛞᚠ
	ᚳ•ᛇᛖᛉᛚᚫ•ᛖᚩᛁᛋ•ᛡᛁᛟᛋᚪᛒᛗ•ᛗᚣᚹᛂ•ᛖᚫᛝ
	ᛚ•ᛂᚱᛇ•ᛈᛚᚩᚻ•ᚪᛞ•ᛡᛂ•ᛞᚠᚹᛞᛂᚳ•ᚾᚦᛉ•ᛂ
	ᚻ•ᚷᛚ•ᚠᛖᚦ•ᛇᚻ•ᛝᛖᛒᛚᛞᛁᛗᚠ•ᚹᛒᛗᛟᛁᛖᛁᛠ•
	ᛈᚻᛝᛖᛞᛟᚩᚻᛂ•ᚹᚩᚾᛂᛈᛗ•ᛖᚳ•ᛖᛇ•ᚷᚻᛗ""",
	
	# p30
	"""ᛞᚪᛈᛖ•ᛗ•ᛉᚫᛒᛇᚱ•ᛖᚣᛟᚣ•ᚱᛠᛈᚢᛠ•ᚣ
	ᛖᚪᚻ•ᚩᛉᛠᚢᚻᛡᛟ•ᚷᚫᚩᛒᛉ•ᚫᚱᛞᛋᚩᚱ•ᚷ
	ᛠ•ᛉᚻᛁ•ᚷᚳᛞᛠᛡᚳ•ᛂᛠᛉᛇᚻᛋᚹ•ᛝᛡᚷ
	ᛖᛡᚣ•ᛠᚩᚷ•ᚱᚦᚠᛟᚩᚦ•ᚦᛁᛏᚱ•ᛇᛉᛇ•ᚢᚷᛠ•
	ᛟᛏ•ᚩᚠᛚ•ᛟᛝᛈ•ᚱᛡᚪᚩᛏ•ᚩᛠᚷᚫᛗ•ᛈᛋᚱ•ᛖ
	ᚦᚠ•ᛞᚹᚾᛚ•ᛝᚩᛇᛂ•ᚳᛚᚢᚹᛏ•ᚩᛖᛏᚠᚪᛚ•ᛟᛇᛟ•
	ᛠᚱᛇ•ᚢᚪᚦᛈᛟᛡᛉ•ᛡᛒᚱᛒᚠᚢᛚᚢᛟ•ᛒᛇᛒ•
	ᛉᚦᚹ•ᛝᚣᛖ•ᚳᚫᚣᛟ•ᚹᛁᛝᚫᛏ•ᚫᛇᛈᛡᛟᚠ•ᛚ•ᛝ
	ᚠᛡ•ᛞᚪᛚᛈ•ᛋᛁ•ᚢᚣᚪᛚᛠᛝᚹ•ᚪᛏᛈᚳᚣ•ᛝᚫ
	ᚻᛗᛞᚷᛚ•ᛠᛉᛒ•ᛇᛡᛋᛖ•ᚣᛁᛚ•ᚣᛠᚣ•ᚻ•
	ᚣᛉᚾᛏᚫᛉᛋᚦᚪᚹᛗ•ᚪᚱ•ᚪᚩᚻ•ᛗᛖᚫᛞᛠᛁᛗ
	•ᛒᛟᚾᚳᚩᚱᛉ•ᛋᚹᚫ•ᚻᛖ•ᛋᚠᚾ•ᚢᚦᛟᚷᛖᚪᛟᛇᛇ•""",
	
	# p31
	"""ᚦᚳᛒᛝᛏᛉᛡᛞ•ᛋᛡ•ᚩᚠ•ᛈᛖᛞᛋᛁ•ᛚᛁᚻᚾᛝᚱ•
	ᚻᛈ•ᛇᚢᚫᛞ•ᛚᚻᛉᚳᛈ•ᛁᛗᛉᚳ•ᛂᚫᚾᛞᛋ•ᛏᛚ
	ᛡᚩᛋᛗ•ᛚᛞᚾ•ᛈᚫᛏᚷᛈ•ᚫᚦᛂᛗ•ᛒᚻᚩᚻᛁᚷᚻᚳ•
	ᛚᚹᛋᚱᛇᛗᛏ•ᛂᚳᛁ•ᛠᚦᛞ•ᛏᛚ•ᚱᛖᛠᛒᚪ•ᛒᚠᛒ•ᛁ
	ᛒᛡᛇᛏᚣ•ᛏᛖᚣᚳᚱᛋᚠ•ᛁᚦᚪᛉ•ᚪᚣᚫᛠ•ᛂ•ᛈ
	ᛗ•ᚠᛋ•ᚪᛒᚱ•ᛉᚣᚻ•ᚦᚩ•ᛇᛞᚢ•ᚠᛁ•ᚻᚩᚫᚠᚣᚷ
	ᚱᚪᛂ•ᛏᛉᛇ•ᛖᛠᛞ•ᛏᚠᚢᛝ•ᚫᛂᛖᛈᚳᛒᚦᚢ
	ᛝ•ᛡᛒᚹᚱ•ᛖᚾᛈᛇᚣᛇ•ᛉᚱᚹ•ᛒᛡᛞ•ᛖᚱᚩᚻᚣ
	ᛠᛈᚦ•ᛗᛁᚷᛚ•ᚹᛉᚫ•ᚠᛞᚾ•ᛂᛟ•ᚻᛚᛡ•ᛗᛖᚷ•
	ᛟᛁᛡ•ᚻᛟᚱᛇᚹᚣᚠ•ᛈ•ᛂᚷᚦ•ᚪᛒᛝ•ᛈᛒᚪᛖ•ᚢᚹᚻ
	ᚩᛒᛋᛉ•ᚹᛞ•ᚦᛇᚱᛖ•ᛂᚾᛞᛝᚹᚪ•ᚻᛖᚹ•ᛟᛡᛂ
	ᛡᛟᛝᛂᛉᛚᛂ•ᛞᛉᛟᛈ•ᚱᚪᛁᛏᚷᛉᛝᛇ•ᛠᛗᚩ""",
	
	# p32
	"""ᛚ•ᚦᚫᚹ•ᚫᚢᛈᛡᚳ•ᚹᛝᚻᚹᛒᛗᛋᛟᛖᛁᛡ•ᛟᚹᚦᚻᛒ
	•ᛡᚱᛏᚦᚠ•ᚠᚩᚦ•ᚻᚩᛗᛖᛉᚹᛞᛋᛚᚠᛞ•ᛝᛒᛇᛡ
	ᛚᚪ•ᚹᛞᚾᚫᛉᛏᚣᛗᚷ•ᚦᚹᛉᛡᚦ•ᚹᛒᛋᚱᛉᛡᛉ
	ᚪ•ᚢᛒᚻᛠ•ᚹᛝᚢᚻᛇᛝᛡᛠᛂ•ᛋᛈᚦᛏ•ᛟᛝᚩ
	ᛗᛒᚢᛞᛋ•ᛒᛂ•ᛠᚱᛟ•ᛖᚾ•ᚾᚹᚷᚢᛚᚪᚩᚣ•ᚢᛏ
	ᚠᛂᛏ•ᚪᚷᛒᛇ•""",
	
	# p33
	"""ᛞᛇ•ᛉᚳᚠᛁᚪᚹᚻᚷ•ᛇᛟ•ᚠᛏᛖᛟᛠᚪ
	ᛡᛋᚷ•ᚣᛠᚾᚦᚫᚱ•ᚩᛡᛗ•ᚹᛉᛗ•ᚣ
	ᛞᛒᛏᚱ•ᚢᛂᚻ•ᚫᛟ•ᛡᛝᚹᚻᛋᚠᛡ•ᛚᚦ
	ᛏ•ᛁᚹᛏ•ᚩᚢᚾᚹᛗᛚ•ᛋᚦᛠᚹᛂ•ᚪᛂᚫᚷᚣᛗᚹᛞ•
	ᛈᛡ•ᛖᛂᚹ•ᛖᚢ•ᚻᚹ•ᛝᛁ•ᛋᚫᚷ•ᛂᛚ•
	ᛝᚦᛇ•ᛁᚠᚳᛟᛇ•ᛞᚹᚣᛡᚣᚢ•ᚣᚾᚦᚱᛖ
	ᛗᛁ•ᛇᛞᚱᚹ•ᛉᚹᚻ•ᚳᛂᛡᚪ•ᚾᚹ•ᚾᛗ•ᚠ
	ᛇᛁ•ᛇᚪ•ᚩᛋᛒᛟ•ᛏᛂ•ᛈ•ᛖᛈᛂᚩᚹᚢᛠ
	ᛝᚹ•ᛗᚳᚩᛏᛏᚠᚢᛂ•ᛞᛠᛉᚩ•ᛉᚦᚷᛞ•ᛒᚩᛏᛚ
	ᛇᛁᛒᛡᚪ•ᛖᚠᛠᚢᛖ•ᛈᛋᚹᛞᛞ•ᛋᛡ•ᚹᚦᛞᛋ•ᛝ
	ᛂ•ᛚᚷᚢᛡ•ᚾᛉᚠ•ᚱᚪᚣᛗᚠᚦᚻ•ᚱᚪᚱ•ᚫᚪᚷᛟᛞ•ᛒ""",
	
	# p34
	"""ᛗᛒ•ᚾᚻ•ᛇᛞ•ᚻᛗᛚᛁ•ᛠᚾᛁ•ᚫᛖᚢ•ᛏᚦᛇᛋᛈᚻ
	•ᚻᛇᚳᛠᚫ•ᛞᛚᛋᛝ•ᛁᚹ•ᚪᚳᚩᛏᛇᛝᚷ•ᚳᚦᛋᛠᚠ
	ᚢᛝᛚᚻ•ᚹᚩᛇᚪᛈᚷ•ᛇᛗᛚᛂᛋᛏ•ᛚᚳᛈ•ᚾᛋᛝ•ᚳᚪ
	ᚳ•ᚾᛉ•ᚾᚢᛉᚫᛗᛏᛞᛏᚫ•ᛟᛗᛋᛉ•ᛏᚣᛉ•ᛇ
	ᛠᚷ•ᚻᛒᚾᚷᛇᚢᛟ•ᛂᚦᛉᚩ•ᚾᚪ•ᛞ•ᚩᛈ•ᛠᛚᛋ
	ᛏ•ᛒᚷᛁᚢᛟᛖᛁ•ᛂᚦᛖᚻᚹ•ᛂᚫᛂᚾᚻᛉᚹ•ᛒᚪᛋ•ᚠᚱ
	ᚱᛁᛉᚢᚦᚻ•ᚢᛗᚪ•ᛞᛝᛠᚪ•ᚫᛉᛖᚾᚹ•ᛟ•ᛝᛞ
	ᚾ•ᛈᚫᚳᛡ•ᛈᚠᛉᚩ•ᛒᚷᛗᚫ•ᛚᚻᛞᚣᛖᛉᛒ•ᛂᚹ
	ᛇ•ᛈᚩᛁᚦᚠ•ᚷᚾᛈᛞᛝᛏᛖᚪ•ᛂᛋᛠ•ᛈᛝᚢ•ᛒᚷ
	ᚳᛉ•ᚪᚢᛈᛚ•ᛂᚱᚷᚣᚪ•ᚪᚠ•ᛗᛝᚣᚳᛟ•ᚹᚣᚷ
	ᛈ•ᛗᛖᚩᚹᚢ•ᛟᛞᛋᚱ•ᚣᛞᛋᚳᛡᛉ•ᚻᚦᚹᛚᛞ
	ᛠᚩᛞᛠᚢᛟᛖ•ᛠᚹ•ᛉᚻᛡᚹᛞ•ᚪᛗ•ᚠᚦᛈ•""",
	
	# p35
	"""ᛝᛏᚳᚪ•ᛠᚣᚷ•ᚳᚦᛖᚾᚢᛁᚫᛁᚢᛡ•ᚹᛚᚳ•ᚻᛈ•ᛞ
	ᛂᚳ•ᛗᛒ•ᛗᚪᛂ•ᚩᚪᛞᛁ•ᚩᚱᛟᚠᛖᚣᛟᛁ•ᛇᛟ•ᛁᛈᚣ
	ᛚᚪᛡ•ᚳᛏᛠᛋᛖᛒᛝ•ᚫᛟᚫᛞᛖᛞᚣᛡ•ᛠᚪᛖ
	ᚦᛚᚫ•ᚳᛋᚪᚩᚷᚹᛚ•ᛈᛖ'ᛏ•ᛂᛉᛝᛚ•ᛏᛉᚩᚣᛝ
	ᚠᚩᚣ•ᛁᚻ•ᛟᚫᚷᛂᛝᛡᚾᛗᚣᛟᛡ•ᛝᚷᛖᛉ•ᛟᛉ
	ᛈᛚᛋᛉᛠ•ᛚᛡ•ᚱᚪᛞ•ᛠᚷ•ᚱ•ᚳᛇᚻ•ᛗᚪᛟᚷ•
	ᛞᚪᛋᛡᚻ•ᛈᚷᛖᚳᛟᚱᛟᚢ•ᛁᚫᛟᚦ•ᛂᚱᛡ•ᚱᛖᚦ
	ᛒ•ᚣᛏᛝᛡᚩᛏᚦᚳ•ᛉᚳ•ᛋᚪᚫ•ᛗᚠᛂᚱᛖ•ᛡᛇᛁᛇ
	ᛟᛉᚳᚹᚪᛖ•ᛋᚢᛉ•ᛋᛟᛚ•ᛂᚾ•ᛈᛇᛒ•ᚦᚦ•ᛁᚫᛚᛋᛝ
	ᛂᛂᛡ•ᛟᚻᛇᚢᛚ•ᛁᚱ•ᛡᚻᛚᛏᚹᛉᛇ•ᚱᛏᛠ•ᛁᚫᛚ
	ᛗ•ᛁᚱᚷᛏᛠ•ᛇᛟᚻᛟᚳᛋᛏᚾᚩ•ᛁᚱᚷ•ᚹ•ᛞᚢᚣᛚᛁ
	ᛗᛒᚢ•ᛚᚱ•ᛏᛁᚢ•ᚷᚳᚠᛇ•ᛚᛇᚣᛏ•ᛏᚫᚢ•ᚫᛠᛇ""",
	
	# p36
	"""ᛖᚾ•ᚢᚹᛝᚻ•ᚷᚣᚱ•ᚩᛁ•ᛚᚾᛉ•ᚾᚩᛈ•ᚠᛠᚫᚫᚩ•ᛉ
	ᚾᛋᛟᚫᛚ•ᚾᚫ•ᚦᚢᛠᚣᚫ•ᛈᛁᛇᚢᚱᛂ•ᛈᛟᛂᚪᛝᛈ
	ᚦᛈᚪᛝ•ᚣᛗᛟ•ᛉᛒᚢᛏᛇᛗᛈᚫᚣ•ᛉᚫᚣᚱᚫᚣ
	ᚠᚠᛗᛡ•ᛉᛖ•ᚱᚢᛏᚷᚢᚣᚱ•ᛡᚢᚩᛇᛁ•ᛂᚠᛈᛂ
	ᛞ•ᛁᚦᚩᚻᛡᚷᚻ•
	1 ᛚᚦᛇᛟ•ᚪᚫᛠ•ᛗᛉᚻᚳᛉᚪᛏᚦ•ᚫᛉ•ᚩᛋᚳᛞ
	ᛏ•ᚣᚹᚾ•ᛟᛏᛉ•ᚹᛁᛟᛂᚠᛁᚩ•ᛁᚱᛋ•ᛉᚾᛗᚪᛡ•ᚱᛈᛋ
	ᛞ•ᛁᛟ•ᚻᛖᛏᚢᚹ•ᛠᛟᛞᛟᛂᛁᛝᛡ•ᛂᚱᛞᛗᛒ•ᚩ
	ᚳᚩ•ᚦᛟᚱᚢᛚ•ᚢᚦᛋᚢᛞᛚ•ᚷᛁᚣᛝᚩᛟ•ᛁᛖᚣ•ᛖᚠ•
	ᛇᛝᛒᛚᛁᚢᚣᚠᛟᚾᛟ•ᛒᛟᚷᛂᚪᚾᛗᚫ•ᚣᚦᚠ•ᛁᛒᛝᛈ
	ᚾᛁᚱᚷ•ᛂᛇᚫ•ᚻᚪ•ᚱᛉᛉ•ᚩᛚᚾᚫ•ᛞᚣᛒᚾᚪ•""",
	
	# p37
	"""2 ᚾᚣᛖᛉ•ᚾᚢᛉᛁ•ᛝᛏᛈᚹᛋᚣ•ᛏᛠᛈᛉ•ᚪᛁ
	ᛂᛋᚱᚪᛏᛋᛝᛏ•ᚳᚷᚳᚻ•ᛖᛟᚱᚪᛡᚻᚳ•ᛝᛒᛖᚱ
	ᛠᚪ•ᛚᛟᛖᛚᚪ•ᚦᛋ•ᚳᚹᚱᚹ•ᚩᚻᚣ•ᚢᛝᚩ•ᛈᛚᛁᛏᚪ
	•ᚠᛋᛝᛞ•ᚳᚪᚱᛒ•ᚹᛈ•ᚾᚩᚦᚳᚦᚾᛗᚩᛖ•ᚣᛇᚾ•ᚠᛒ
	3 ᛞᚢᛈ•ᚹᚾᛖᚪ•ᚱᛚᛁᚹ•ᚫᛉ•ᛝᚠᛞᚪᚠ•ᛒᛂᛉ•ᛞ
	ᛂᛝᚣᛇᚪ•ᚫᛂ•ᛝᛈᚪ•ᚢᛠ•ᛇᛏᚱ•ᛖ•ᚫᛗ•ᚫᛠ
	ᚻ•ᛁᚫᛟ•ᛠᚹᚳᛂᚦᚻ•ᛡᚩᚢ•ᚩᚦᚷᛡ•ᚻᛋᚷᚪᛁᛟᛞ
	ᚪᛂ•ᛁᚹᛡᛒ•ᛗᛝᛡᛞᚠᛒᛋᛏ•ᛒᚷᚠ•ᚷᛟᚢᚳᚫᛏᛁ
	ᛖ•ᚱᚷᛗᚣ•ᚪᚷᚹ•
	4 ᛝᛂᛋᛂᛗᚱᛗ•ᚾᛒᛋᛗᛉᛞᚻᛉᛁ•ᚣᛡᚻᚣ
	ᛠᛉᚻ•ᛞᛖ•ᚹᛖᚦ•ᚢᚳ•ᛉᛗᚪᚣᛠ•ᚹᚫᚪᚳ•""",
	
	# p38
	"""ᚢᚫᚳᛇᚳᚣ•ᛡᚫᛏᛖᚳᚠ•ᛋᚻ•ᛋᚱᚢᚦ•ᛁᛋᛝᛗᛞ
	ᚫᚢᛠᚢᚪ•ᚾᛝᚳ•ᛖᛈᚹᛉ•ᚢᛉᚫ•ᚾᛈᚳᚻᚱᚣ
	ᚹᛚᛉᚱᛒ•ᛗᚫᛟᚣᚩ•ᚳᛇᛗ•
	5 ᚻᚫᛉᚦᛒᛟ•ᛏᛟᚹᛂ•ᚫᛠᛗᚠᚫᚳᚷ•ᛇ•ᚻᚹᛗ
	ᚻᛝᚣ•ᛁᚩᛁ•ᛏᛁᛖᛡᛂ•ᛗᚣᛚ•ᚻᚱᚩᛞᛒᛡᛈᛠᛗ•
	ᚳᛠ•ᛖᛒᚢ•ᚷᛁᚦ•ᛟᚫ•ᛡᚻᛝᛖᚾ•ᚱᛠᛡᛋ•ᚻᛏ
	ᛝᚻᚪᚷᚩᛝᚫ•ᚹᛚᛏᚱ•ᚷᛁᚾ•ᛖᛠᛂᛡᛞᛋᚻ•ᛝᚾ
	ᚳᛋᚾᛞᛇᚾᛋᛁᚳᛡ•ᚱᛝᛚᚫᚣᛇᛚᚩ•ᚳᛞᚾ•ᛝᚷᛡ•
	ᛝᛂ•ᚻᛂᛚᛠᛟ•ᛂᛏᚷ•ᛚᛒᛝᚢᛏ•ᚻᚳ•
	•ᚫᛞᛟᚫᛟᛗ•ᛟᚫᚪᚻᚱᛗᚢ•ᚣᚢᚣ•ᛈᛗ•ᚪᛂᚫᛟ
	ᛠᛚᚠᛖᛡᚢ•ᛉᚻ•ᚪᚩᛡᛒᛠᚢᚷ•ᚻᛏᛠᚪᛞ•""",
	
	# p39
	"""ᛋᚹ•ᚦ•ᚾᛋᛁᚻᛒ•ᛉᛠᛝ•ᛒᚢᛚᛟᚢᚾ•ᚢᚦᚩᛗᚪ•ᚾ
	ᛞᚫᛇ•ᚫᚣᚪᛋ•ᚣᛝᛡᛗᚷᛇᛈ•ᛠᚳᚻᛝᛚ•ᚠᚷ
	ᛡ•ᛁᛡᚪᚠᛒᛈ•ᚳᛋᚦᛠᚦᚫᚱ•ᚷᛞᛚᛟ•ᚷᚱᛁᛇ•ᚣᚩ
	ᛟᚢᛝᚱᚷ•ᛗᛏᚷᛒᛈᚷ•ᛗᛏ•ᛗᚣᚹᛒᛏᛒ•ᚷᚣᛈ
	ᚷ•ᚾᚦᛇᛒᚳ•ᚷᛖᛇᛟᛚᛈ•ᚹᚾ•ᚻᚷᚱᛇᛏ•ᛈᚷᛒ•ᚹ
	ᛗᛋᚹᛟᚻ•ᛡᚳᛋ•ᛈᛞᛋᛡ•ᚪᚹᛏᚳᚹᛟ•ᛗᚹᛁᛒᛞ•ᚷ
	ᛇᚢᛚ•ᛉᛋᚫ•ᛟᚻᛚᚦᛒ•ᚣᚪᛚᛞᚦᚠ•ᚻ•
	ᛞᛝᚩᚢᛋᚪᚫ•ᛖᚦᛁ•ᛏᛂᛏ•ᛝᚦᚾᚳᛉ
	ᛏᛝ•ᚳᛈᛁ•ᚾᛏ•ᛒᚾᛡᚱᛒ•ᚢᛈᛋᚦᛁᚳᛈᛋᛁᚹ•ᚹᛚᚣᚾ
	ᚢ•ᛒᛁᚪᛠ•ᚹᛟᚳ•ᛠᚢᚪ•ᛚᚦᚹ•ᚠᚾᛏᚳᛡᛁ•ᛚᚩ•ᚾ
	ᛗᛂᛠ•ᚦᛟᛂ•ᚪᚦᚹ•ᛡᚾᛖᛠᛈ•ᛒᛋᛂ•""",
	
	# p40
	"""ᚠᚾᛗ•ᚣᚷᛞᚫᚻ•ᚪᛈᛉᚣᚻ•ᛇᛠᚩᛖ•ᛏᛝ
	ᛠ•ᛚᛁᛏᚦᚠ•ᛗᚪᚳᛖ•ᛞᚳ•ᛏᚱᛟᚷᛠᚾ
	ᚫᛒᚢᛖᛒᚢ•ᚦᚠᛟ•ᚷᛋᛟ•ᛁᛈ•ᛟᛉᛋᛒ•ᚹᛂᛒ
	ᚣᛗᚢᛠ•ᚱᛁᚢᛟᛂᛁ•ᛗᛖᚫ•ᚱᛋᛉᛝ•"ᛠᛈᛚ•
	ᛞᚩᛚᛁᛉᛠᛝᛖᚱ"•ᚾᛈᛖᚹᛡ•ᚾᛂᛏᚣ•ᛋᚩᛋ
	ᛏᛝ•ᚢᚾᛇᚪ•ᛖᛏᚪᛂᚳᚣ•ᛟᛒ•ᛚᛋ•ᛒᛞᛂ•ᛁᛝᚣᛖ
	ᚳ•ᛂᚻᛚᚣ•ᚷᚫᛚᛞ•ᛚᚫᛚᚦᛉ•ᛚ•ᛖᛉᚩᛉᛁᚳᚢᛗ
	ᚾᚢ•ᚩᚾᛇ•ᚻᛡᛚᛇᚩᚫᚪ•ᚩᛟᚩ•ᚣᚱ•ᛖᚠᚢ•ᛁᚻ•ᛟᛚ
	ᚾᛏ•"ᚠᛞᚱᛠᚷ•ᛈᚩᛇᚩᛗᛠᛒ•ᛂᛡ•ᛋᛗᚠ•ᛏ
	ᚠᚫᚩ•ᛟᚳᛚᛞᛡᛚ•ᚩᚳᛝᚢ•ᛈᚹᛏ•ᚷᚳᛋ•ᚢᛟᚷᚦ•
	ᚠᛉᚠᛏ•ᚳᛋᛉᛟ•ᚷᚠᛉᚾᛞ•ᛒᛏᛠᛡ"•ᛈᛡ""",
	
	# p41
	"""ᛠᛁᚪ•ᛋᚣᛗᛞᚣᛋ•ᛒᛞᛂᛞ•ᚩᚾᛏᛚ•ᚳᚪᛝ•ᚱᚷ
	ᚻᚷ•ᛂᚹᚠ•ᚪᚢᛇ•ᛞᛏᛗᛂᛁ•ᛝᚫ•ᛉᛈᚳᛈᛠ•ᛟᚪ
	ᛒᛁᛁᛋ•ᛇᚷᚻᛋ•ᛇᛡᛒ•ᚠᚹᛝ•ᚫᚪᚠᚩᚣᛡᚪᚾᚻ•ᛒᚦᛟ
	ᛇᚣᛟᛁᛒ•ᛟ•ᚩᛋᚹ•ᛞᚳᚠᚪᛁ•ᛉᛏᛟᚢᚩᛟᚦᛈᛋᚩ•
	ᚻᛇᚦᛝ•ᛏᛠᚠᛝᛠ•ᚩᛗ•ᛏᚠᚣᛚᚣ•ᚹᛚᛞ•ᚪᛉ
	ᛠ•ᚪᛂ•ᚩᛋᛒᛚ•ᚳᛖᚾᚪᚩᚱᛏᚦ•ᚱᛒᚳᚣ•ᛠᛗᚹᛚ•
	ᚻᛈ•ᛇᛈᛖ•ᛚᛂᚩᛡᚪ•ᛖᛋᚫᚩ•ᛠᛉᛝᚣ•ᛖᚫᛒ
	ᛗ•ᛖᚻᚱ•ᛈᚾᛗ•ᚹᛏᛟᚣᚢ•ᚠᛉᛈᛗᚩᚷᚾ•ᛡᛇᚳ
	ᚠᛒᛈᛗ•ᛋᛇᛁ•ᛖᛈᚢᚱᛏᚳᚣ•ᛂᛚᚠ•ᚱᛚᚱᚫᛖᚻᛟ
	•ᛇᚣᛡ•ᚩᛉ•ᚪᛋᚣᛁᛝ•ᛉᛚᛂ'ᚳ•ᛖᚣᚢᛝᚦᛇᚱ•
	ᛠᛁᚫ•ᚦᚠᛟᚷᛠᛁ•ᛈᛋᛒ•ᛗᛒᛂᚠᚾᚳᛖ•ᚻᚫᚩᛂ•
	ᛉᛂᛚᛈᚪᛁ•ᛟᚹᚱᛁᚱᚦᛖᛉ•ᚪᚾ•ᛞᛂᚷ•ᛟᛟᚳᛏᛂ""",
	
	# p42
	"""ᛞ•ᛉᚾᛗᚦ•ᛁᛂᚱ•ᛈᛉᚢᚫᚦᛒᚠᛂᚦ•ᚠᚪᛝᛖ•ᚹᚹᚣ
	ᛚᛇ•ᚢᚣ•ᚾᚱᚪ•ᛈᚾᚹ•ᛚᚾᛏᛚᚢᛒᚱᛝᚪᛋ•ᚫᛈ•ᛂᛚ
	ᚢᚳᚷ•ᛚᛏᛂᚹᛈ•ᚫᛗᛚ•ᛉᛚᛗᛏᛞᚠᛈᛁ•"ᚠᚳᚦ
	ᛗᛂᚹᚱᚪᛚ•ᚩᛝᚱᚢᛈᚱᛟᛡ•ᚳᛉᚱ•ᛇᛏᚦᚾ•ᚱᛇᚫ
	ᛞᛟᚻ•ᛒᚾᚣ•ᚠᛡᚪᛡᛖᚫᛞᛂᚢᛖ•ᚦᚱ•ᚩᛇᚱᛡ•
	ᚣᛁᛉᛇᚻᚩᛠ•ᚫᚻᛡᛝᛠᚦ•ᚾᚣ•ᚾᚠᛁᛝ"•"ᛏ
	ᚻᚹᚫ•ᛒᛇ•ᛡᚻᛉᛒ•ᛞᛝᚱᛂᚦᚻ•ᚪᚷᚣᛁᚠᚷ•ᛁᛏᛞ
	ᛠᛒᚠᚩᛈ•ᛇᛡᛟᚹᚱᚾᚩᛏ•ᛋᚹᚢ•ᛖᛡᛖᛡᚦ•ᛉ
	ᚪᚷᛈᚾ•ᛋᚱᚠᛞᛝᚻᛖᛂᛞ•ᛂᛡ•ᚱᚹ•ᚷᛝᚪᛒ•ᛂᛈ
	ᛂ•ᛏᚠᛉ•ᚪᛂ•ᛁᚠᛉᚢᚩᚣᚻᚦ•ᚻᚾᛁᛒ•ᛡᛟᛡᛋᛈᚣ
	ᛉ•ᛠᚢᛠᛚ•ᚠᛝᛗᚻ•ᚦᛒᚩ•ᛗᛚ•ᚩᛠᛋᚦᛠ•ᛇ
	ᛋᛉ•ᚠᛗᛒ•ᚫᛋᛇᚾᛡᚾ•ᚢᚫᚹ•ᛞᛠᚢᚾᛝᚠᚾᛖᚫ""",
	
	# p43
	"""ᚻᛂ•ᛁᛖᛏᛡ•ᚷᛁᚩᚾ•ᚳᚢᚫᛗᛈᛋᚪᛡ•ᚷᛚᚣᚹᛟ"•
	ᚠᚢ•ᛉᚠᚫᛞᚠᛡᛂᚾ•ᚻᛋᚦᚠ•ᛏᚠᛂᚱᚹᚠᛋᚾᚹᛂ
	ᛖᛒᚢᚦ•ᚩᛇᚫᛈ•ᛡᛟ•ᚢᛁᚩᛂᚩᛇᛟᛂᛞᚩ•ᛈᚹᛞ
	ᚷᚱ•ᚠᛟ•ᛇᚷ•ᛂᛟᛇᚫᛋᚫᚣ•ᛒᛏᛞᛟ•ᛠᚻᛡᚱᛠ
	ᛠᛉᛋ•ᚠᚾᚣᚱᚠ•ᚪᚾᛡᚪᛖᚫ•ᚳᛇᛁᛝ•ᛒᛡᛞᛠ
	ᚫᛒᛠᚳᛉᚠ•ᚫᛏᛁᚱᚪᛗᚩ•ᛚᛉᛋᚪ•ᛒᚩᛈᚫᚩᛝᚻᛇ
	ᛖᛇᚫ•ᚻᛖᛇᛠ•ᚱᛗᛞ•ᚫᛇᛗ•ᚾᚾᚣᛡ•ᚱᚾᛗ
	ᛠ•ᛂᛉᛋᛂ•ᛟᛖᛒ•ᛏᚻᚾ•ᚠᚪᚠ•ᛒᚾ•ᚩᚾ•ᛖᛋᛏᛒᚹ
	ᛡ•ᚻᛏ•ᚩᛟᚩ•ᛒᚾᛖᚳᛁᚹᚣᛟ•ᛟᚩᛒ•ᛋᛖᚩ•ᚫᚻᛟ
	ᚠᚫᚷᚩᛂ•ᛟᛒᚻ•ᚳᛖᛁᛚᚫᚣᛚ•ᚢᛚᛁ•ᚾᛟᛏ•ᚫᛈᛟᛈ
	ᛝᛗ•ᚳᚢᛁ•ᚣᛋᚳᚢᛡᛇᚩ•ᚠᛖ•ᚷᛟ•ᚻᚫ•ᛝᚠ•ᛗᚠ
	ᛝᛉᛞᛁ•ᛗᛝᚣᚪᛝᚠᛉᛁᛟᚷᛚ•ᛇᚩ•ᚫᛡᛏ•ᛂᛏ""",
	
	# p44
	"""ᛠᚢ•ᚷᚦᚣ•ᚦᚾᛟᚣᚩᛖᚻ•ᛁᛋᛖᚣᚦᚪᛡᛝᛟᛇᛚ•
	ᛡᛏᛝ•ᛁᛚ•ᚠᛉᛡᛠᛏ•ᚠᚾᛂᚠᚻᚳ•ᚻᛞᛠᚣᛟ
	ᛝ•ᛉᛇᚻᚩᛋᚻ•ᛇᛏᚠ•ᛚᚱᛇᚦᚪᛁᛁ•ᛒᚠᛁᛚ•ᛂᛡᛒᚣ
	ᛗᚫᚫ•ᛞᚻᛟ•ᚪᚹᛉᛚᛏᛁᚪ•ᛟᛞᛖᚾᛈᚻᚣ•ᚦᛚᛖᛋ
	ᛖᛟᚫᛖ•ᛏᚱᚪ•ᛁᚫᚹᚫ•ᛋᛈᚱ•ᛂᛡᚪᛏ•ᚫᚦ•ᚠᛠᚢ
	ᛈᚣᚫᛝ•ᚣᚾᚻᛡ•ᚳᛗᚠᚾ•ᛞᛂ•ᛖᚩ•ᛒᚷᚻᚪ•ᛖᛞ
	ᛟᚠᛇᛞᛟ•ᛈᚳᛁᚪᛒᚷᛒᛈᛟ•ᛟᛂᚠᚪᛖ•ᛂᚣᚩᛂ•ᚣ
	•ᚫᛋ•ᚦᛁᚫᛂᚫᛏ•ᛖᛇᚻᛟ•ᚣᚠᚹᛞᚷ•ᛡᚱᛒᚢ•ᛒᛚ
	ᚢ•ᚷᛈᛂᚪ•ᛏᛡ•ᚳᛂᚠᛡᛝᛚᚣᛒ•ᛗᚻ•ᚱᛚᛟᛠᛋ
	ᚦᛝ•ᛏᚳᛟᛉᛁ•ᛂᚱᚳᛖᛏᛂᚷ•ᛡᛈᛏᛉᚩᛁᛂᛟ•ᚷ
	ᚩᚪᚢ•ᚣᛖᚪᛋᛟᛇᚢᚪᛡ•ᛗᚱᛚᚳᚠ•ᛒᛗᛝ•ᚻᛉ•
	ᛠᛂᚫ•ᛉᚪᚷᚻᚣᛏᛖᛝ•ᛉᛉᛗᚾᚫᛋ•ᚱᛗᛞᛋ""",
	
	# p45
	"""ᚳ•ᚦᛚᛟ•ᛝᛇᚢ•ᚻᚩ•ᛏ•ᚢᛁᚦᛂᚾᚠᚱᚦ•ᛋᛟᚷᛠ
	ᛗᚪ•ᛝᛚᚪᛁᛒᛠᚢᛋ•ᚩ•ᛖᛋᛝ•ᚠᛡᚢᛟᛞᛇᚪ•ᛞ
	ᛡᛒᚹᚩ•ᛂᛋ•ᛟᛝᛏᚳ•ᚻᚾᛇᛋ•ᛗᛚᚻᛞᛖᛈ•ᚫᛂᚱ
	ᚪᚢᚻᚱᚦᚱ•ᛟᛂ•ᛟᛗᚩᛟᛏ•ᚫᛇ•ᛉᛒᚳ•ᛂᛁ•ᚪᚩᛉ•
	ᚹᚪᚾᛈᛏᚢᚣ•ᛁᛒᚢ•ᚦᚩᛡ•ᛗᚳᚠᛉᚱᛁ•ᚪᛗᛏᛒ•
	ᛗᛚᛁᚦᛏᛠᛋᚾᚷᛚ•ᛏ•ᛇᛈ•ᚩᛚᛞ•ᛚᚹᚳᛂᚹᛉ•ᚪ
	ᛡᚹᛇ•ᛖᛖᚹ•ᛏᚪ•ᚣᚠᛉᚳ•ᛗᚩᚷᛞᚷ•ᛚᚳ•ᛒᚣᛋ
	ᚣᚠᛞᚣᛝ•ᛠᛇᛏᚩᚢᚫ•ᛟᛁᛒ•ᛏᚾᚫᚠ•ᛂᛟᛗᚾ
	ᛈ•ᛠᛡᚩᛏᛡᚪᚱᛞ•ᚪᛝᛈᚹᛗᛂᛟᛠᚩ•ᛚᚹᛉ•
	ᚱᛗ•ᚩᛏᚹᛂᚹᚾ•ᚷᚳᛠ•ᛂᚳᚢᚱ•ᛟᛇᛟᚾᚻᚫᛉ•
	ᚣᛚᚩ•ᚩᛡᚳᚻᛂ•ᛋᚣᚹᛁ•ᚣᚠᛋᚾᚪ•ᚷᛖᚾᛂᚪᚹᛠ•
	ᛞᚠᛟ•ᚢᛁ•ᛖᛇᚦ•ᚫᛞ•ᚳᛂ•ᚷᚢᚻᚣᚻᛁᛒᛉᚾ•ᚹᛝ""",
	
	# p46
	"""ᚻᛏᛉᚫᛁᛂᚢ•ᛞᚠᛡᚫ•ᛋᛁᚹᛝᛈ•ᛗᛉᛂᛈ•ᛞᛗ
	ᛝ•ᛇᛚᛞᚣ•ᚠᚩᛞ•ᛝᚷᚾᛇ•ᚷᛖ•ᛚᛉᚣ•ᚫᛚᛖᛉ•
	ᛡᛝᛋ•ᚳᛁᚦ•ᚷᛏᚣ•ᚹᚩ•ᛝᛖ•ᛒᚪᛗᛏᚪᚷᛒ•ᛈᛡ
	ᛟ•ᚪᛉᛝᛒᛞᛉᛂᚦᚢ•ᛏᛇᛖ•ᚣᚪᚳ•ᛠᚦᚹ•ᛏᛉ
	ᚩᚳᛞᛒ•ᛟᚩᛠᚾᚠᚪ•ᛚᛗᛖᛁᚦᚫᚪᛡᛂᛁᚪᚱ•ᚦᚱᛖ
	ᛖᚣᛋᚾ•ᛖᛏᚢᚻᛈᚳᚦᛋ•ᚳᛇᛉᛖᛇᚠ•ᛞᛠᛏ
	ᛈ•ᚣᛇᛠᚢᛏ•ᛉᚦᚷᚻ•ᚫᚾᛠᚱ•ᛡᛒᛏᛁᛉ•ᚩᚢ
	ᛝ•ᛚᛒᛇᚩ•ᛟᛉ•ᚦᛞᚷᚠ•ᚩᚱᛈᚪᛏ•ᚫᛋᚪᚦ•ᛖᛟᚪᛝ
	ᚫ•ᚣᛒᛚ•ᛡᚦᚾᚠᛈᛟᛡᚾ•ᛖᚹ•ᛖᛗᚩ•ᛉᚹᚦᛠ•ᛁᚦ
	ᛒᛖᚱ•ᛟᚳᛉ•ᛈᛖ•ᛁᚢᚦ•ᛈᚠᛞᛈᛂ•ᛁᛟᚻ•ᛒᚦᛏᚩ
	ᚳᚢᛚ•ᛞᛂᛝ•ᚦᛂᛁᚪ•ᚹᚣ•ᚢᛝᚾ•ᛋᚾᛈᚠᚫᛒᛂᚫ•ᛡ
	ᛗᚹ•ᛇᚪᚩᚾᛂᚳᛚᛒᛉ•ᚣᛠᚦᚹ•ᛝᛚᛗᚳᛡᛇᚠᚫ""",
	
	# p47
	"""ᛠᛁᚦ•ᛒᛠᛚᚦᚳᛞᛁᛇ•ᚠᚢᛉᛋᛉᛁᚦᚫᛋᛗ•ᚦᚹ•
	ᛈ•ᛒᛋᛏᚫᚾᚱᛁ•ᚦᛇᛡᚱᛚᛡᚹ•ᚢᚩᛋᚱ•ᚹᚫ•ᛒᚹᛡᛖ
	ᛟᛂ•ᛡᚣᛖᚩᛖᛡᚷᚫᚠᚾᚹ•ᛟᛏᚫᚠᛂᚹᛠ•ᚦᛞ•ᛁ
	ᚫᚩᚾ•ᛋᚷᛈᚪᛖᚩ•ᚣᚦᚹ•ᚾᚷ•ᛠᛋᚩᛇᛏ•ᛝᛚᚷᛞ
	•ᛒᛈᛈ•ᛗᛁᚪᛖ•ᛚᛏᛁ•ᚫᛂᛖ•ᛒᚾᚠᚪᛋᚷᛒᚠ•ᚫᚹᚣᚷ
	ᚢᛡᚠᛠ•ᛖᛋᛞ•ᛚᚳᛒᛞᛏᛈ•ᛖᚾᛈᚣ•ᚱᚠᚻ•ᚫ
	ᛝ•ᛟᚪᛗ•ᛒ•ᛡᛚ•ᛝᛋᚱᚢᚹᚱᚣᚻᚹ•ᚹᛡᛈ•ᛁᚻᚾᚻᚱ
	•ᚳᛖᛏᚫᚩᛋ•ᚣᛋ•ᛝᚫᛡᛝᚫ•ᚻᚦ•ᛇᚪᛞᛋ•ᛒᛁᚳᛈ
	•ᛇᛒᛟᚫ•ᛠᛝᛖ•ᛝᛠᚣ•ᛒᚣᛉᚻᚢᚠᚦᛞᚹ•ᛗ
	ᚢᛁᛡᛂᚩ•ᛋᛇᚫᛇᛝᚱ•ᛚᛇᛠ•ᛏᚩᛂ•ᚩᛝᛈ•ᚱᚻ
	ᛠᚢᛉᚦ•ᚣᚢᛋ•ᛡᛚᛖᚷᛗᛝᚹᚻᚱᛋ•ᚢᛟᚣᛠ
	ᚷᚩᚷ•ᛇᛁᛖ•ᛠᛂᛇᛁᚾᛂᚩᛗᚱᛡᛉ•ᚠᚻᚳ•ᚪᚩᚪᚫ""",
	
	# p48
	"""ᚻᚳᛁᚦ•ᛂᚷ•ᛝᛖᚢ•ᛡᛏᛁ•ᛚᚩᚱᛈ•ᚠᚪ•ᛈᛞᚱᛒ•
	ᛝᛁᛋ•ᚷ•ᚠᚾᛈᚠᛒ•ᛟᚦᛁᛠᚪ•ᛡᛏᚾᚳ•ᚦᛟᚻᛈᛖᛚ
	ᚫ•ᛟᚠᛗ•ᛡᛝ•ᛒᛝᚦᛝᛠᚠ•ᛇᛗᛟ•ᚩᛠᛈ•ᛁᛡᚱ
	•ᚹᚹᛟᚩᛒᚩ•ᚾᚩᛂᛟᚾ•ᚦᛡᚠ•ᚩᛂᛞᚦᛏᛁ•ᛈᚾᚪᚱᛂ•
	ᛉᚱᚣ•ᛝᛡ•ᛏᛗ•ᛈᛞᚣᚻ•ᛗᛝᚫᚳᛇ•ᛡᚣᛂᛟ
	•ᛝᚩᚢᛇᛁᚱ•ᛏᚪ•ᚩᚻᚪᛚᚫᛚᚪ•ᛋᛈ•ᛏᚪᛂᚳᚦᚢᛏᚹ
	ᚦ•ᛗᚷᛖᛗᚣᛡᛁᛞ•ᚢᛋᚠᛒ•ᛟᛚᛟ•ᚪᛒ•ᚦᛚᚣ•ᚳ
	ᛠᚣ•ᛞᛇᛁ•ᚹᛉ•ᛟᛝᛒᚢᛋᛞᚻᛞ•ᚢ•ᛠᚱ•ᚫᚩ
	ᚻᛝᛒᚪᚹ•ᛈᛡᚾᛚᛇ•ᛖᛟᛝ•ᛡᚠᛇᛡ•ᚳᚦᚹ•ᛚᚦᚪᛁ
	ᛈ•ᛞᛟᛂ•ᚢᛉᚢᚾᛠᚠ•ᚩᚾᚪ•ᚱᛠᚷ•ᛗᚢ•ᛗᛁᛂ
	ᛒᛗᚱᚾᛗ•ᚩᚾᚠᚣ•ᛗᚠᛇᚠᛂ•ᛒᛡᛈᛂᛖᛡᛏ•ᛈᛟ
	ᚫᛏᛟ•ᚻᛖᚾ•ᚳᛇᚩ•ᛋᚻᚫᛇ•ᛝᛁᛟ•ᛇᚠᚢᛞᚣᚪᛚᚠ""",
	
	# p49
	"""ᛡ•ᛖᛂ•ᚠᛚᛟ•ᛁᚳ•ᛁᛝᚷᚦ•ᛗᛋᚫᚷᚪᛠ•ᛗᛁ•ᛒᛡᛏ
	ᚾ•ᛝᛗᚦ•ᛏᚣᚫᛂ•ᛖᚻᚠᚪᛡᚷ•ᚪᛗᛁ•ᛞᛉᛏ•ᚢᛖ
	ᚦᚾ•ᛖᚪᛈᚹᛠᛚ•ᛒᚢᚱᛡᛟ•ᚪᚣ•ᛟᛇᚹᛂᛈᛞ•""",
	
	# p51
	"""ᚹᚹᛈ•ᚠᛡᛚᛉᛒᚾ•ᚳᛗᚾᚱᛗ•ᚻᚦᚫᛞᛂ•ᛒᛡᚫ•ᛇᚹ
	ᛗᚢ•ᚪᛈᛡ•ᛈᛁᛂ•ᚪᚢᚾᛠᛖᛞᛗᚪ•ᛏᛟᛗ•ᛋᛞ
	ᛝᚷᛚᛋᛞᛝ•ᛟ•ᛋᛂᛞ•ᛚᛟᚠᛂᚫᚠᚪ•ᛝᛟᚣᛈ•ᚣᚩ
	ᛒᚷᚳᛖᛏᚹ•ᚪᛋᛒ•ᛗᛠᚣᛇᛗᚫᛚᚱ•ᚹᛇᛂᛒ•ᛈᛚᚠ""",
	
	# p52
	"""ᛈ•ᚠᛗ•ᛝᚪᛇᚾᛟᚹᛇᛉ•ᚣᚫᛉᛞᛟᚱᛒ•ᛡᚱᛟ•ᚹᛏ
	ᚷᚱᛂᛖ•ᛠ•ᛈᛚᛞ•ᚻᚦᚱ•ᚦᚣᛚᛉ•ᛠᛈᚫᚠᚪ•ᚫᚪ
	ᛒ•ᛈᛋ•ᛗ•ᛏᚫᚳᛈᛝᚹᚦ•ᚻᛠ•ᛞᚩᛂᚷ•ᛋᚩᛠᚳ
	ᛖᛋ•ᚣᛖᚫ•ᛈᚦ•ᛁᛇᛈᚳᛝ•ᛈᚳᛇᚢᛏᚳᛡᛇᛝᚾ
	ᚢᚻᚦ•ᚣᚠᛗᚾ•ᛝᚠᛂᛉᛟᚱᛗ•ᛝᛠᛂᛏᚳ•ᚢᚷ
	ᚦ•ᚠᚦᛋ•ᚪᛈᚩᚪᚫᛞᛋᛝ•ᛒᛗᚩᚷ•ᚹᚠᛗᛖ•ᛠᛇᚻᚠ
	ᚻᚳᚱᚫ•ᛝᛗᛉᚳ•ᛋᚪᚹᛋᛠ•ᚩᚣᛚᛉᛝ•ᛠᛟᛉ
	ᛟᛠᛡᛝᛒ•ᛝᚳᚫᛁᚱ•ᛒᚠ•ᛏᚣᚣ•ᛠᛒ•ᚣᛚᚩ•ᛇ
	ᛉ•ᚩᚷᛗᚩ•ᚠᛚᛟᛝᚦᛠ•ᚦᚣᛖᚣ•ᚾᚷᚾ•ᛡᛏ•ᛂ
	ᛟᚾᛁ•ᛋᛟ•ᛠᚦᚣ•ᛋᛒ•ᚫᛚᚪᛂᛡᛖᚷᛉᛡᚾᛉᛏ•
	ᛡᛒᚻᛚᚷ•ᚢᚦᛠ•ᚢᚾᛁᚩᛗᛠᛁᚷ•ᛟᚦᚱᚣ•ᛒᛖ
	ᛠᚩᛈ•ᛗᛏᚱᚫᚢᚻᛁᛝ•ᛇᚳᚠ•ᛂᚾᚱᚷ•ᛟᚷᚻᚣᚻ""",
	
	# p53
	"""ᛇᚫᛠᚫᚣ•ᚢᛗᛈ•ᛉᛁᚢᚾᚩᛟᚾ•ᚷᛞᚦ•ᛡᚫᚹ•ᛞ
	ᛟᛖᚱ•ᛗᚾᛖᚻᚷᛒᚢᛂ•ᚢᚦᛗᛖᛞᛝ•ᛒᚷᚣᚱ•ᛖ
	ᛁᚢᛂ•ᚣᛡᛚᚢ•ᛂᛟ•"ᛠᛉᚣᛇᚱ•ᚩᛈᛋᚳᚫᛗ
	ᛇ•ᚾᛂ•ᛖᚠᛋ•ᛖᚠᚪᛝ•ᚢᛝᛂᛇᚷᚠᛝᚱᛁᚦ•ᛂᚢᚫ•
	ᚣᛋᚠᛖᚢᛋᚫᚣᛠ•ᛁᛏᛟᚱᛏᛟᚩ•ᚷᚾᚻ•ᛞᛗᚩᚳ
	ᛞᛖᛏ•ᚹᛉᛞᛚ•ᚩᚫᛂ•ᛇᚢᛒ"•ᛗᛏ•ᛞᛗᛖ•ᛏ
	ᛈᚹᛇᛋ•ᚹᛒᛇᚦ•ᚾᚻᚷᛂ•ᚱᛡᛞᛡᚦᚪᛁᛇᚫᛉᛚ•ᛇ
	ᛠ•ᛡᚪᛂ•ᚻᚱ•ᚦᛈᛞᛂᛝᚩ•ᚷᚠᛇᛗᚳ•ᚻᛞᚩᛏᚳ
	•ᚢᚱ•ᛈᚾ•""",
	
	# p54
	"""ᚪ•ᛗᛝᛞᛡᚦᛉᛁᛗ•ᛡᛞᛈᛝᚢᚹᚪᛗ•ᛏᚪ
	ᛝ•ᛝᚦᛡᚹᛋᚻ•ᛁᚳ•ᚫᛈᚫᚷᚩ•ᛗᛁᚪ•ᛖᚩ•ᛏᚹ
	ᚩ•ᚠᚣᚢᛏᛂ•ᚦᛂᛠᛖᚳᚾᛠ•ᚳᛠᛖ•ᚱ
	ᚩᚢᛉ•ᛞᚹᚻᛒᛝᚠᚪᚳᛂᚢ•ᚩᛂᛡᛠᛁᛚᚷᚻ•ᛒᚢ
	ᛂ•ᛉᚪᚳᚹᛡ•ᛗᚩᛈᚣᛞᛡᛚᛈ•ᛇᛁᚦᚱ•ᚣᚷᛗ•ᛉ
	ᛟᚷᛋ•ᛗᛈᛂᛟᛞ•ᛟᛏᛡᛟ•ᛏᛝᛁ•ᛗᛝᚣᚪᚫ•ᛝ•ᚱ
	ᚣᛂ•ᚾᛚᚢᛉᛒ•ᚻᛈᛂᚩᛠ•ᚷᚫᚹ•ᛉᛋᛞᚳ•ᚢᛏ•
	ᛟᚻᛇᚾᛈᛏ•ᛠᚣᛒᚢᚷ•ᚷᚪᛇ•ᚾᚷᚩᛖᛚᛗᛒᚦ•ᚣ
	ᛡᛟᛇᚣ•ᛗᚳᛟᚦ•ᛖᛚᚱᛇᛈᚱᛞᚣ•ᛉᛞ•ᛝᚣᛈ•
	ᛋᛖᛉᚹ•ᚳᚷᚠᛞᚱᛖ•ᛞᛖᚹᚩᛇᛟ•ᚻᚩᛟ•ᛒᛋ•ᚻ
	ᛠᚪᚳᛁᛗᛉᛂᛗᛖ•ᛗᛚ•ᚷᚩᛏᚦᛉᛖᛠᚱᚷᚣᛝ•ᚫ""",
	
	# p55
	"""ᛗᛁᚹ•ᛋᛒ•ᛉᛗ•ᛋᛇᚷᛞᚦᚫ•ᚠᛡᚪᛒᚳᚢ•ᚹᚱ•ᛒ
	ᛠᚠᛉᛁᛗᚢᚳᛈᚻᛝᛚᛇ•ᛗᛋᛞᛡᛈᚠ•ᛒᚻᛇᚳ•
	ᛇᛖ•ᛠᛖᛁᚷᛉᚷᛋ•ᛖᛋᛇᚦᚦᛖᛋ•ᚦᛟ•ᚳᛠᛁᛗ
	ᚳᛉ•ᛞᛂᚢ•ᛒᛖᛁ•""",
	
	# p56
	"""ᚫᛂ•ᛟᛋᚱ•ᛗᚣᛚᚩᚻ•ᚩᚫ•ᚳᚦᚷᚹ•ᚹᛚᚫ•ᛚ
	ᚩᚪᛈ•ᛗᛞᛞᚢᚷᚹ•ᛚ•ᛞᚾᚣᛂ•ᚳᚠᛡ•ᚫᛏ
	ᛈᛇᚪᚦ•ᚳᚫ
	ᚳᛞ•ᚠᚾ•ᛡᛖ•ᚠᚾᚳᛝ•ᚱ   •ᚫᛁᚱᛞᛖ•ᛋᚣᛂᛠᚢ
	ᛝᚹ•ᛉᚩ•ᛗᛠᚹᚠ•ᚱᚷᛡ•ᛝᚱᛒ•ᚫᚾᚢᛋ•""",
	
	# p57
	"""ᛈᚪᚱᚪᛒᛚᛖ• ᛚᛁᚳᛖ•ᚦᛖ•ᛁᚾᛋᛏᚪᚱ•ᛏ
	ᚢᚾᚾᛖᛚᛝ•ᛏᚩ•ᚦᛖ•ᛋᚢᚱᚠᚪᚳᛖ•
	ᚹᛖ•ᛗᚢᛋᛏ•ᛋᚻᛖᛞ•ᚩᚢᚱ•ᚩᚹᚾ•ᚳ
	ᛁᚱᚳᚢᛗᚠᛖᚱᛖᚾᚳᛖᛋ• ᚠᛁᚾᛞ•ᚦ
	ᛖ•ᛞᛁᚢᛁᚾᛁᛏᚣ•ᚹᛁᚦᛁᚾ•ᚪᚾᛞ•ᛖᛗᛖᚱᚷᛖ•"""
]

# Assigning 2nd argument to target page to make it easier to run
# All these stuff checks the argument and manages wrong entries

exists = 0
param = "p0"
list = 0

if len(sys.argv)<2:
	print("\n\tUsage python3 runescript.py p* where * is the number of page.")
	print("   Remember that p50 does not have runes, so it does not exists in runescript.\n")
	print("   You may use as argument: p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11,")
	print("   p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26,")
	print("   p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41,")
	print("   p42, p43, p44, p45, p46, p47, p48, p49, p51, p52, p53, p54, p55, p56, p57")
	print("   or own.\n")
	sys.exit(0)

for check in range(len(dict)):
	if dict[check] == sys.argv[1]:
		exists = 1
		list = check

if (exists == 1):
	target = book[list]
else:
	print("\n\tUsage python3 runescript.py p* where * is the number of page.")
	print("   Remember that p50 does not have runes, so it does not exists in runescript.\n")
	print("   You may use as argument: p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11,")
	print("   p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26,")
	print("   p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41,")
	print("   p42, p43, p44, p45, p46, p47, p48, p49, p51, p52, p53, p54, p55, p56, p57")
	print("   or own.\n")
	sys.exit(0)


# Subtract is for skipping spaces and •s in the text, so that our offsets stay on track
# There's probably a cleaer way to do it but CBF

subtract = 0

# Open a file to store informations on it

f = open('translated.txt', 'w')

# forge_offset() makes a list of offsets to be *added* to the corresponding rune when shifting
# i.e. If your offset list is [3, 4, 28, 4, 6, 9] you'll shift the first offset by 3, the second by 4, etc
# It takes three arguments: A base list, a 'direction' and another offset
#
# Base list: What your basic offset looks like, say a list of primes
# Direction: Either -1 or 1, this is will be multiplied to the final number so you can add or subtract offsets
# Offset: Offset every number in your list by this
#
# Special note: Instead of a list, you can supply a piece of alphabetical text to the function
# We work out what number of the alphabet it is and return a list based on that instead
# to supply a different text put it on "own" in book array (way up) then call own as parameter

# Target is the target page which I've parametrized the functions
# target = p54

# Write to file which sequence is being used
f.write('sequence: ' + str(sequence) + "\n\n")

# Side is the direction, to add or subtract each rune value
for side in range(2):

	# Determine its direction
	if(side == 0):
		direction = -1
	else:
		direction = 1

	# Write to a file
	f.write('\nDirection: ' + str(direction) + "\n\n")

	# param is the second offset, it rotates the entire list giving us 29 possibilities
	# this loop should compute all possibilities
	for param in range(29):

		# Clear the output and subtract to next sequence
		output = ""
		subtract = 0

		offsets = forge_offsets(sequence, direction, -param)

		# The stuff below is a little more confusing
		# We pull each rune from the text supplied
		# If it's a •, add a space to the output
		# If it's a rune (i.e. searching for it returns true), then we find the corresponding letter after applying the offset
		# If it's not a rune (• or anything else), then we also maintain our subtract value
		#
		# Just trust me this works
			
		for rune_num in range(len(target)):
		  rune = target[rune_num]
		  offset = offsets[rune_num - subtract]
		  if (rune == "•") or (rune == " "):
		    output+=" "
		    subtract += 1
		  elif (rune == "0") or (rune == "1") or (rune == "2") or (rune == "3") or (rune == "4") or (rune == "5") or (rune == "6") or (rune == "7") or (rune == "8") or (rune == "9"):
		    output+=rune
		    subtract += 1
		  elif type(find_position(rune)) is int:
		    output+=table[(find_position(rune) + offset) % 29][1]
		  else:
		    subtract += 1

		# We then print the output of our stuff
		# All the frequency() function does is return frequencies in numbers
		# So here we format it to look a little nicer
		
		# Next line of code is used with page 54, which starts with A or I
		# it checks if its an A or an I followed by a whitespace then it only writes
		# the sequences which means something into a file, reducing the ammount of data to read
		# if (output[0] == 'A' and output[1] == ' ') or (output[0] == 'I' and output[1] == ' '):
		f.write(str(param))
		f.write("\n")
		f.write(output)
		f.write("\n\n")

		print(param)
		print(output)
		print("\n")
		 
		freq = frequency(output)
			
		for entry in freq:
			print(entry + ": " + str(round(freq[entry] / len(output) * 100, 4)))

		print("\n")
	
f.close()