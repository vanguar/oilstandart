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
$to = 'tzvanguardia@gmail.com'; // put your email
$email_subject = "��� ���������� ����� - ����������� ���: $name";
$email_body = "��������� ����� \"����������� ���\". \n\n".
 "������ �����������:\n\n���: $name \n".
 "�������: $phone";
$headers = "From: tzvanguardia@gmail.com\n";
$headers .= "Reply-To:"; 
mail($to,$email_subject,$email_body,$headers);
return true; 
?>