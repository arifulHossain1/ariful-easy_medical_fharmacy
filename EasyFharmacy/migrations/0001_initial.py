# Generated by Django 3.1.7 on 2021-03-22 17:22

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('license_no', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('medicine_details', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('request_date', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('joining_date', models.DateField()),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('medical_type', models.CharField(max_length=200)),
                ('buy_price', models.CharField(max_length=200)),
                ('sell_price', models.CharField(max_length=200)),
                ('batch_no', models.CharField(max_length=200)),
                ('shelf_no', models.CharField(max_length=200)),
                ('exp_date', models.DateField()),
                ('mfg_date', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('in_stock_total', models.IntegerField()),
                ('qty_in_strip', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.company')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDetails',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('salt_name', models.CharField(max_length=200)),
                ('salt_qty', models.CharField(max_length=200)),
                ('salt_qty_type', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.medicine')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_date', models.DateField()),
                ('salary_amount', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.employee')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBank',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_number', models.CharField(max_length=200)),
                ('ifsc_number', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.employee')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBank',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_number', models.CharField(max_length=200)),
                ('ifsc_number', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.company')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAccount',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=200)),
                ('transaction_amt', models.CharField(max_length=200)),
                ('transaction_date', models.DateField()),
                ('payment_mode', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.company')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.bill')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.medicine')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyFharmacy.customer'),
        ),
    ]