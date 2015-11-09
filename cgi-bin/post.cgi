#!/bin/sh -x
 
cat << _EOF1_
Content-Type: text/html

<!doctype html>
<html>
<head>
<title>user</title>
</head>
<body>
_EOF1_

echo ${aaa}
echo ${REQUEST_METHOD}
 

cat << _EOF2_
</body>
</html>
_EOF2_
