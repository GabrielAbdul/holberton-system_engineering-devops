#!/usr/bin/env ruby
# test strings: hbn, hbon, hbtn, hbttn, hbtttn, hbttttn
# match result: hbn, hbtn, hbttn, hbtttn, hbttttn
puts ARGV[0].scan(hbt*n/).join
