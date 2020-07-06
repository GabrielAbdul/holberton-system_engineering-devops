#!/usr/bin/env ruby
# must be exactly matching a string that starts with h ends with n and can have any single character in between
# any single character stands out as .
puts ARGV[0].scan(/^h.n$/).join
