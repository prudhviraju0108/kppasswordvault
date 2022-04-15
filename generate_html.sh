#!/bin/bash
mysql_user="root"
mysql_passwd="test"
db="passwordvault"
tbl="details"
/usr/local/mysql/bin/mysql -u${mysql_user} -p${mysql_passwd} -e "select name from ${db}.${tbl}" 2>/dev/null | grep -iv name > /tmp/apps_list
echo '<BODY bgcolor="#ccffcc">
      <form method="POST" action="">
      <label for="App">Choose app to fetch data:</label> 
      <select id="cars">' > /tmp/kp_index
for i in `cat /tmp/apps_list`
do
echo " <option value=\"$i\">$i</option>" >> /tmp/kp_index
done
echo '</select>
	<H1>Update new details here </H1> <br>
         App_Name <input type="text" name="name">
         <br>
         user_name <input type="text" name="user_name">
         <br>
         password <input type="text" name="password">
         <br>
         <input type="submit">
         </form>' >> /tmp/kp_index
