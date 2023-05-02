# Generated by Django 4.1 on 2023-05-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_category_banner"),
    ]

    operations = [
        migrations.AddField(
            model_name="billingaddress",
            name="province",
            field=models.CharField(
                choices=[
                    ("กรุงเทพมหานคร", "กรุงเทพมหานคร"),
                    ("กาญจนบุรี", "กาญจนบุรี"),
                    ("กาฬสินธุ์", "กาฬสินธุ์"),
                    ("กำแพงเพชร", "กำแพงเพชร"),
                    ("ขอนแก่น", "ขอนแก่น"),
                    ("จันทบุรี", "จันทบุรี"),
                    ("ฉะเชิงเทรา", "ฉะเชิงเทรา"),
                    ("ชลบุรี", "ชลบุรี"),
                    ("ชัยนาท", "ชัยนาท"),
                    ("ชัยภูมิ", "ชัยภูมิ"),
                    ("ชุมพร", "ชุมพร"),
                    ("เชียงราย", "เชียงราย"),
                    ("เชียงใหม่", "เชียงใหม่"),
                    ("ตรัง", "ตรัง"),
                    ("ตราด", "ตราด"),
                    ("ตาก", "ตาก"),
                    ("นครนายก", "นครนายก"),
                    ("นครปฐม", "นครปฐม"),
                    ("นครพนม", "นครพนม"),
                    ("นครราชสีมา", "นครราชสีมา"),
                    ("นครศรีธรรมราช", "นครศรีธรรมราช"),
                    ("นครสวรรค์", "นครสวรรค์"),
                    ("นนทบุรี", "นนทบุรี"),
                    ("นราธิวาส", "นราธิวาส"),
                    ("น่าน", "น่าน"),
                    ("บึงกาฬ", "บึงกาฬ"),
                    ("บุรีรัมย์", "บุรีรัมย์"),
                    ("ปทุมธานี", "ปทุมธานี"),
                    ("ประจวบคีรีขันธ์", "ประจวบคีรีขันธ์"),
                    ("ปราจีนบุรี", "ปราจีนบุรี"),
                    ("ปัตตานี", "ปัตตานี"),
                    ("พระนครศรีอยุธยา", "พระนครศรีอยุธยา"),
                    ("พะเยา", "พะเยา"),
                    ("พังงา", "พังงา"),
                    ("พัทลุง", "พัทลุง"),
                    ("พิจิตร", "พิจิตร"),
                    ("พิษณุโลก", "พิษณุโลก"),
                    ("เพชรบุรี", "เพชรบุรี"),
                    ("เพชรบูรณ์", "เพชรบูรณ์"),
                    ("แพร่", "แพร่"),
                    ("ภูเก็ต", "ภูเก็ต"),
                    ("มหาสารคาม", "มหาสารคาม"),
                    ("มุกดาหาร", "มุกดาหาร"),
                    ("แม่ฮ่องสอน", "แม่ฮ่องสอน"),
                    ("ยโสธร", "ยโสธร"),
                    ("ยะลา", "ยะลา"),
                    ("ร้อยเอ็ด", "ร้อยเอ็ด"),
                    ("ระนอง", "ระนอง"),
                    ("ระยอง", "ระยอง"),
                    ("ราชบุรี", "ราชบุรี"),
                    ("ลพบุรี", "ลพบุรี"),
                    ("เลย", "เลย"),
                    ("ลำปาง", "ลำปาง"),
                    ("ลำพูน", "ลำพูน"),
                    ("ศรีสะเกษ", "ศรีสะเกษ"),
                    ("สกลนคร", "สกลนคร"),
                    ("สงขลา", "สงขลา"),
                    ("สตูล", "สตูล"),
                    ("สมุทรปราการ", "สมุทรปราการ"),
                    ("สมุทรสงคราม", "สมุทรสงคราม"),
                    ("สมุทรสาคร", "สมุทรสาคร"),
                    ("สระแก้ว", "สระแก้ว"),
                    ("สระบุรี", "สระบุรี"),
                    ("สิงห์บุรี", "สิงห์บุรี"),
                    ("สุโขทัย", "สุโขทัย"),
                    ("สุพรรณบุรี", "สุพรรณบุรี"),
                    ("สุราษฎร์ธานี", "สุราษฎร์ธานี"),
                    ("สุรินทร์", "สุรินทร์"),
                    ("หนองคาย", "หนองคาย"),
                    ("หนองบัวลำภู", "หนองบัวลำภู"),
                    ("อ่างทอง", "อ่างทอง"),
                    ("อำนาจเจริญ", "อำนาจเจริญ"),
                    ("อุดรธานี", "อุดรธานี"),
                    ("อุตรดิตถ์", "อุตรดิตถ์"),
                    ("อุทัยธานี", "อุทัยธานี"),
                    ("อุบลราชธานี", "อุบลราชธานี"),
                ],
                default="1",
                max_length=50,
            ),
        ),
    ]
