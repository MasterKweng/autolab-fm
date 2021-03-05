# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

FMERP = {
    "conn_str":"mysql+pymysql://fmpets_test_admin:fmpets_test_admin123456@rm-bp1l97bfvo5tc47dsbo.mysql.rds.aliyuncs.com:3306/fmpets_erp",
    "encoding": "utf-8",
    "echo": False,
    "tables": ["t_acc_fmt", "t_bank_account"]
}
FMERP_T_ACC_FMT = {
    "table_name": "t_acc_fmt",
    "columns": ["acc_number", "company_id", "data_org", "date_created", "db_table_name_prefix", "id", "in_use", "memo", "subject_code"],
    "primary_key": ["id"],
    "nullable": ["date_created", "memo", "data_org", "in_use", "db_table_name_prefix"],
    "unique": [""],
    "index": [""],
    "default": {"date_created": None, "memo": None, "data_org": None, "in_use": '1'}
}
FMERP_T_BANK_ACCOUNT = {
    "table_name": "t_bank_account",
    "columns": ["id", "bank_name", "bank_number", "memo", "date_created", "data_org", "company_id"],
    "primary_key": ["id"],
    "nullable": ["date_created"],
    "unique": [""],
    "index": [""],
    "default": {"date_created": None}
}