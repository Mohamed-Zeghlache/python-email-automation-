import smtplib
from email.message import EmailMessage
import pandas as pd

# locating my cv file
cv_file = r'C:\Users\Mohamed\Desktop\CV\Mohamed Zeghlache _ Data Analyst.pdf'

# openning and reading my cv file
with open(cv_file, 'rb') as f:
  file_data = f.read()
  file_name = f.name

# gmail address and gmail app password
email_address = "email address"
email_password = "gmail app password"

# read the emails list csv file
df = pd.read_csv(r"C:\Users\Mohamed\Desktop\emails_list.csv")


i =1
for e in df["Website/Email"]:
  msg = EmailMessage()
  msg['Subject'] = 'Data Analyst / Python Developer'
  msg['From'] = email_address


  msg.add_alternative("""\
     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML><HEAD><TITLE>Email Signature</TITLE>

<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
</HEAD>
<BODY style="font-family:Verdana, Helvetica, sans-serif;">
<table style="font-family:Verdana, Helvetica, sans-serif;" cellpadding="0" cellspacing="0">
 <tbody>
  <tr>
   <td style="width:140px; padding:0; font-family:Verdana; text-align:center; vertical-align:middle;" valign="middle" width="140">
    <img alt="Photograph" width="100" height="100" border="0" style="width:100px; height:100px; border-radius:50px; border:0;"  src="https://media-exp1.licdn.com/dms/image/C4D03AQGJq4fx7zDVfg/profile-displayphoto-shrink_200_200/0/1583933108020?e=1611187200&v=beta&t=qeXjYNbr3bSP6xuPWkiltdN7BSX9hNpMMfwrgKmTyYY">
   </td>
   <td style="font-family:Verdana; border-bottom:2px solid #ed5a24; padding:0; vertical-align:top;" valign="top"> 
    <table style="font-family:Verdana, Helvetica, sans-serif;" cellpadding="0" cellspacing="0">
     <tbody>
      <tr>
       <td style="font-family:Verdana; padding-bottom:6px; padding-top:0; padding-left:0; padding-right:0; vertical-align:top;" valign="top">
        <strong><span style="font-family:Verdana; color:#ed5a24; font-size:14pt; font-style:italic;">Mohamed Zeghlache</span></strong><br><br>    <span style="font-family:Verdana; color:#ed5a24; font-size:10pt;">Data Analyst / Python Developer</span>  
       </td>      
      </tr>     
      <tr>     
       <td style="font-family:Verdana; padding-bottom:6px; padding-top:0; padding-left:0; padding-right:0; line-height:18px; vertical-align:top;" valign="top">    
        <span style="font-family:Verdana; font-size:10pt;">email: mohamedzizouinfo@gmail.com<br> </span>        
        <span style="font-family:Verdana; font-size:10pt;">phone: +213797695824<span style="font-family:Verdana; font-size:10pt;">  </span> </span> 
       </td>
      </tr>
      <tr>     
       <td style="font-family:Verdana; padding-bottom:6px; padding-top:0; padding-left:0; padding-right:0; line-height:18px; vertical-align:top;" valign="top">    
        <span style="font-family:Verdana; font-size:10pt;">Adili Ali, Saihi 1, Biskra</span><br>
        <span style="font-family:Verdana; font-size:10pt;">Algeria</span>      
       </td>
      </tr>
     </tbody>
    </table>                
   </td>  
  </tr>
  <tr>
   <td style="font-family:Verdana; width:140px; padding-top:6px; padding-left:0; padding-right:0; text-align:center; vertical-align:middle;" valign="middle" width="140"> 
    <span><a href="https://www.facebook.com/mohamed.zizou.3705" target="_blank"> <img border="0" width="20" alt="Facebook icon" style="border:0; height:20px; width:20px" src="https://img.icons8.com/color/48/000000/facebook-new.png"></a></span>
    <span><a href="https://twitter.com/moh_zeghlache" target="_blank"><img border="0" width="20" alt="Twitter icon" style="border:0; height:20px; width:20px" src="https://img.icons8.com/fluent/48/000000/twitter.png"></a></span>
    <span><a href="https://www.linkedin.com/in/mohamed-zeghlache/" target="_blank"><img border="0" width="20" alt="LinkedIn icon" style="border:0; height:20px; width:20px" src="https://img.icons8.com/color/48/000000/linkedin.png"></a></span> 
    <span><a href="https://www.instagram.com/mohamed.zeghlache/" target="_blank"><img border="0" width="20" alt="Instagram icon" style="border:0; height:20px; width:20px" src="https://img.icons8.com/fluent/48/000000/instagram-new.png"></a></span>
   </td>
   <td style="padding-top:6px; padding-bottom:0; padding-left:0; padding-right:0; font-family:Verdana; vertical-align:middle;" valign="middle">
    <span style="font-family:Verdana; font-size:10pt;"><a href="https://github.com/Mohamed-Zeghlache" target="_blank">github.com/Mohamed-Zeghlache</a></span>
   </td>
    </tr>

 </tbody>
</table>
<h4><br><br>Spontaneous Application: Data Analyst / Python Developer.</h4>
 <p style="max-width:700px;">
    <br>I hold a masters degree in information systems and I would like to be considered for the position of Data Analyst / Python Developer. <br><br>

As you will see from my CV. In my five years at the university, I implemented different projects in the domain of information systems, I have also got a certificate of data analyst from Udacity where I was able to implement eight real-world projects using (Python, R, Tableau, Excel and SQL).<br><br>

I would like to be considered for the position of Data Analyst / Python Developer, as I believe I possess the appropriate skills. Over the last year, I have implemented many projects throughout my studies. This meant wrangling, analyzing and exploring data and coming up with reasonable solutions for better results.<br><br>

I strive for long-term success, I'm a firm believer in life-long learning and always trying to enhance my skills<br><br><br><br>

Yours sincerely,<br><br>

Mohamed Zeghlache<br>
    </p>
</BODY>
</HTML>

  """, subtype='html')

  msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name[-36:-4]+' / Python Developer.pdf')


  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    msg['To'] = e
    smtp.send_message(msg)
    print(str(i) + ' -- sent email to  :  '+ e)
    i += 1