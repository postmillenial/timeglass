pmset -g batt | grep Internal  | cut -f 2 | cut -f 1 -d '%' > output.txt
