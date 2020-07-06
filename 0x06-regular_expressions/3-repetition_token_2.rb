#!/usr/bin/env ruby
# test strings: hbn, hbtn, hbttn, hbtttn, hbttttn
# match result: hbtn, hbttn, hbtttn, hbttttn
puts ARGV[0].scan(/hbt+n/).join
