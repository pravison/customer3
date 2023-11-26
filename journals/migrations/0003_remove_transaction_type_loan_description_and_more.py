# Generated by Django 4.2.4 on 2023-09-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0002_rename_transactions_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='type',
        ),
        migrations.AddField(
            model_name='loan',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='extraCost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='cost',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='costOfGoodSold',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='forWhat',
            field=models.CharField(blank=True, max_length=700),
        ),
        migrations.AddField(
            model_name='transaction',
            name='interestPaidUpfront',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='paidComplete',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionType',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='capitalwithdrawal',
            name='fromWhichAccount',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='capitalwithdrawal',
            name='toWho',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='loan',
            name='dayTaken',
            field=models.DateField(max_length=120),
        ),
        migrations.AlterField(
            model_name='loan',
            name='installmentPaymentDuration',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='loan',
            name='interestPaidUpfront',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='paidUntil',
            field=models.DateField(max_length=120),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='chartsOfAccounts',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='creditAmount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='debitAmount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='fromWhichAccount',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='fromWho',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='toWhichAccount',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='toWho',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
