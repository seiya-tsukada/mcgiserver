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

key=`echo "${QUERY_STRING}" | awk -F "=" '{print $1}'`
value=`echo "${QUERY_STRING}" | awk -F "=" '{print $2}'`

echo "key: ${key}"
echo "value: ${value}"
 

cat << _EOF2_
</body>
</html>
_EOF2_
