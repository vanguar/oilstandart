<?php
// check if fields passed are empty
if(empty($_POST['name'])   ||
   empty($_POST['phone']))
   {
echo "No arguments Provided!";
return false;
   }

$name = $_POST['name'];
$phone = $_POST['phone'];

// create email body and send it 
$to = 'vanguar@ukr.net'; // put your email
$email_subject = "��� ���������� ����� - ����������� ���: $name";
$email_body = "��������� ����� \"����������� ���\". \n\n".
 "������ �����������:\n\n���: $name \n".
 "�������: $phone";
$headers = "From: vanguar@ukr.net\n";
$headers .= "Reply-To:"; 
mail($to,$email_subject,$email_body,$headers);
return true; 
?>