# -*- coding: utf-8 -*-
import os, csv, sqlite3
import itertools
import os, sys


def lower_first(iterator):
    return itertools.chain([next(iterator).lower()], iterator)

def main():
    """

    :Import csv to database
    """

    # Config para execucao de standalone herdando apps, framwork, e configuracoes do django
    proj_path = "."
    # This is so Django knows where to find stuff.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feiraproject.settings")
    sys.path.append(proj_path)

    # This is so my local_settings.py gets loaded.
    os.chdir(proj_path)

    # This is so models get loaded.
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    from feirapp.models import Feira
    csvfile = os.getcwd() + '/import_csv/DEINFO_AB_FEIRASLIVRES_2014.csv'


    with open(csvfile) as csvfile:
        reader = csv.DictReader(lower_first(csvfile))
        for row in reader:
            Feira.objects.update_or_create(**row)


if __name__ == '__main__':
    main()