import boto3
import click
import sys

session = boto3.Session(profile_name='pyhonautomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webtron deployes website to AWS"
    pass

@cli.command('list-bucket')
def list_buckets():
    "list all buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_object(bucket):
    for object in s3.Bucket(bucket).objects.all():
        print(object)

if __name__ == '__main__':
    cli()
