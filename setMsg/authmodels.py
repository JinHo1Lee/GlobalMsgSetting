# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AlertClntcount(models.Model):
    seq = models.AutoField(primary_key=True)
    client_code = models.CharField(max_length=20)
    connect_date = models.DateTimeField(blank=True, null=True)
    smsmt1 = models.IntegerField(blank=True, null=True)
    smsurl1 = models.IntegerField(blank=True, null=True)
    mmsmt1 = models.IntegerField(blank=True, null=True)
    smsmo1 = models.IntegerField(blank=True, null=True)
    mmsmo1 = models.IntegerField(blank=True, null=True)
    sessiontime = models.DateTimeField(blank=True, null=True)
    servername = models.CharField(max_length=20, blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    cnt_flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_clntcount'


class AlertClntsession(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    cnt_mtsession = models.IntegerField(blank=True, null=True)
    cnt_smosession = models.IntegerField(blank=True, null=True)
    cnt_mmosession = models.IntegerField(blank=True, null=True)
    cnt_reportsession = models.IntegerField(blank=True, null=True)
    cnt_flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_clntsession'


class AlertEmma(models.Model):
    alert_id = models.CharField(primary_key=True, max_length=20)
    alertinfo_key = models.IntegerField()
    emmaperiod = models.IntegerField(blank=True, null=True)
    emmacnt = models.IntegerField()
    sms = models.CharField(max_length=1, blank=True, null=True)
    url = models.CharField(max_length=1, blank=True, null=True)
    mms = models.CharField(max_length=1, blank=True, null=True)
    smo = models.CharField(max_length=1, blank=True, null=True)
    mmo = models.CharField(max_length=1, blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    daycheck = models.CharField(max_length=1, blank=True, null=True)
    format1 = models.CharField(max_length=1, blank=True, null=True)
    starttime1 = models.CharField(max_length=2, blank=True, null=True)
    endtime1 = models.CharField(max_length=2, blank=True, null=True)
    format2 = models.CharField(max_length=1, blank=True, null=True)
    starttime2 = models.CharField(max_length=2, blank=True, null=True)
    endtime2 = models.CharField(max_length=2, blank=True, null=True)
    format3 = models.CharField(max_length=1, blank=True, null=True)
    starttime3 = models.CharField(max_length=2, blank=True, null=True)
    endtime3 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_emma'
        unique_together = (('alert_id', 'alertinfo_key'),)


class AlertQueue(models.Model):
    que_name = models.CharField(primary_key=True, max_length=100)
    que_cnt = models.IntegerField()
    que_updatetime = models.DateTimeField(blank=True, null=True)
    que_type = models.CharField(max_length=10, blank=True, null=True)
    que_server = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'alert_queue'
        unique_together = (('que_name', 'que_server'),)


class AlertRecipient(models.Model):
    alertinfo_key = models.IntegerField(primary_key=True)
    alert_recipient = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'alert_recipient'
        unique_together = (('alertinfo_key', 'alert_recipient'),)


class AlertRecipientName(models.Model):
    alert_phone = models.CharField(max_length=20, blank=True, null=True)
    alert_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_recipient_name'


class AlertRelayip(models.Model):
    seq = models.AutoField(primary_key=True)
    relay_id = models.CharField(max_length=20, blank=True, null=True)
    relay_name = models.CharField(max_length=50, blank=True, null=True)
    relay_isvalid = models.CharField(max_length=1, blank=True, null=True)
    relay_access = models.CharField(max_length=100, blank=True, null=True)
    relay_islimit = models.CharField(max_length=1, blank=True, null=True)
    relay_msglimit = models.IntegerField(blank=True, null=True)
    relay_remotehost = models.CharField(max_length=15, blank=True, null=True)
    relay_remotehost1 = models.CharField(max_length=15, blank=True, null=True)
    relay_remotehost2 = models.CharField(max_length=15, blank=True, null=True)
    relay_linetype = models.CharField(max_length=1, blank=True, null=True)
    relay_conndate = models.DateTimeField(blank=True, null=True)
    relay_updatedate = models.DateTimeField(blank=True, null=True)
    servername = models.CharField(max_length=20, blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    updatedate = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    country = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_relayip'
        unique_together = (('relay_id', 'relay_linetype', 'servername', 'relay_remotehost'),)


class AlertSession(models.Model):
    alert_id = models.CharField(primary_key=True, max_length=20)
    alertinfo_key = models.IntegerField()
    mt = models.CharField(max_length=1, blank=True, null=True)
    smo = models.CharField(max_length=1, blank=True, null=True)
    mmo = models.CharField(max_length=1, blank=True, null=True)
    report = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_session'
        unique_together = (('alert_id', 'alertinfo_key'),)


class AlertcodeMsg(models.Model):
    alert_code = models.IntegerField(primary_key=True)
    alert_title = models.CharField(max_length=32)
    message = models.CharField(max_length=20, blank=True, null=True)
    alert_dbcode = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'alertcode_msg'


class Alertinfo(models.Model):
    alertinfo_key = models.AutoField(primary_key=True)
    alert_code = models.IntegerField()
    fault_type = models.IntegerField()
    alert_id = models.CharField(max_length=8)
    allow = models.CharField(max_length=1)
    alert_callback = models.CharField(max_length=25)
    alert_repeat = models.IntegerField()
    alert_period = models.IntegerField(blank=True, null=True)
    alert_sendcnt = models.IntegerField()
    alert_reset = models.IntegerField()
    alert_recvtime = models.DateTimeField()
    alert_sendtime = models.DateTimeField()
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertinfo'


class Alertlog201612(models.Model):
    alert_seq = models.AutoField(primary_key=True)
    alertinfo_key = models.IntegerField()
    emma_key = models.CharField(max_length=32)
    alert_recvtime = models.DateTimeField()
    alert_send = models.CharField(max_length=1)
    alert_id = models.CharField(max_length=8)
    alert_code = models.IntegerField()
    fault_type = models.IntegerField(blank=True, null=True)
    fault_value = models.IntegerField(blank=True, null=True)
    fault_src = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertlog_201612'


class Alertlog201701(models.Model):
    alert_seq = models.AutoField(primary_key=True)
    alertinfo_key = models.IntegerField()
    emma_key = models.CharField(max_length=32)
    alert_recvtime = models.DateTimeField()
    alert_send = models.CharField(max_length=1)
    alert_id = models.CharField(max_length=8)
    alert_code = models.IntegerField()
    fault_type = models.IntegerField(blank=True, null=True)
    fault_value = models.IntegerField(blank=True, null=True)
    fault_src = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertlog_201701'


class Alertlog201805(models.Model):
    alert_seq = models.AutoField(primary_key=True)
    alertinfo_key = models.IntegerField()
    emma_key = models.CharField(max_length=32)
    alert_recvtime = models.DateTimeField()
    alert_send = models.CharField(max_length=1)
    alert_id = models.CharField(max_length=8)
    alert_code = models.IntegerField()
    fault_type = models.IntegerField(blank=True, null=True)
    fault_value = models.IntegerField(blank=True, null=True)
    fault_src = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertlog_201805'


class Alertlog201806(models.Model):
    alert_seq = models.AutoField(primary_key=True)
    alertinfo_key = models.IntegerField()
    emma_key = models.CharField(max_length=32)
    alert_recvtime = models.DateTimeField()
    alert_send = models.CharField(max_length=1)
    alert_id = models.CharField(max_length=8)
    alert_code = models.IntegerField()
    fault_type = models.IntegerField(blank=True, null=True)
    fault_value = models.IntegerField(blank=True, null=True)
    fault_src = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertlog_201806'


class Alertmsg(models.Model):
    alert_code = models.IntegerField(primary_key=True)
    fault_type = models.IntegerField()
    message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertmsg'
        unique_together = (('alert_code', 'fault_type'),)


class Authkey(models.Model):
    publickey = models.TextField()
    privatekey = models.TextField()
    allow = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authkey'


class Authlog201805(models.Model):
    auth_pr = models.AutoField(primary_key=True)
    client_code = models.CharField(max_length=8)
    authdate = models.DateTimeField()
    auth_destip = models.CharField(max_length=15)
    auth_rslt = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'authlog_201805'


class Authlog201806(models.Model):
    auth_pr = models.AutoField(primary_key=True)
    client_code = models.CharField(max_length=8)
    authdate = models.DateTimeField()
    auth_destip = models.CharField(max_length=15)
    auth_rslt = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'authlog_201806'


class Authstat(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    authdate = models.CharField(max_length=6)
    auth_cnt = models.IntegerField()
    success_cnt = models.IntegerField()
    fail_cnt = models.IntegerField()
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authstat'
        unique_together = (('client_code', 'authdate'),)


class Bannuminfo(models.Model):
    bannumber = models.CharField(primary_key=True, max_length=25)
    valid = models.CharField(max_length=1)
    memo = models.CharField(max_length=40, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bannuminfo'


class Callback0Prefix(models.Model):
    prefix = models.CharField(primary_key=True, max_length=3)
    block = models.CharField(max_length=1, blank=True, null=True)
    min_len = models.SmallIntegerField()
    max_len = models.SmallIntegerField()
    rgn_check = models.CharField(max_length=1, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callback_0prefix'


class Clientaddinfo(models.Model):
    client_code = models.CharField(max_length=8)
    info_type = models.SmallIntegerField()
    value = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'clientaddinfo'


class Clientaddrinfo(models.Model):
    client_code = models.CharField(max_length=8)
    info_type = models.SmallIntegerField()
    value = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'clientaddrinfo'


class Clientcreditinfo(models.Model):
    group_code = models.CharField(primary_key=True, max_length=8)
    client_code = models.CharField(max_length=8)
    credit_period = models.SmallIntegerField()
    pdutype = models.IntegerField()
    allow = models.CharField(max_length=1, blank=True, null=True)
    resetcredit = models.CharField(max_length=1, blank=True, null=True)
    resetcredit_date = models.SmallIntegerField()
    givingcredit = models.IntegerField()
    extracredit = models.IntegerField()
    exceed_block = models.CharField(max_length=1, blank=True, null=True)
    exceed_alarm = models.CharField(max_length=1, blank=True, null=True)
    print_seq = models.IntegerField(blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)
    last_deductingtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clientcreditinfo'
        unique_together = (('group_code', 'client_code', 'credit_period', 'pdutype'),)


class Clientgroupinfo(models.Model):
    group_code = models.CharField(primary_key=True, max_length=8)
    group_id = models.CharField(max_length=20)
    group_name = models.CharField(max_length=40)
    allow = models.CharField(max_length=1)
    client_level = models.CharField(max_length=1)
    checkcredit = models.CharField(max_length=1, blank=True, null=True)
    print_seq = models.IntegerField(blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientgroupinfo'


class Clientinfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    group_code = models.CharField(max_length=8)
    client_id = models.CharField(max_length=20)
    client_name = models.CharField(max_length=64)
    client_passwd = models.CharField(max_length=20)
    publickey = models.TextField(blank=True, null=True)
    privatekey = models.TextField(blank=True, null=True)
    allow = models.CharField(max_length=1)
    block = models.CharField(max_length=1)
    spamcheck = models.CharField(max_length=1)
    bannumcheck = models.CharField(max_length=1)
    crypto_method = models.CharField(max_length=4)
    crypto_keysize = models.IntegerField()
    use_ip_auth = models.CharField(max_length=1)
    use_mac_auth = models.CharField(max_length=1)
    use_smsmt = models.CharField(max_length=1)
    use_smsurl = models.CharField(max_length=1)
    use_smsmo = models.CharField(max_length=1)
    use_mmsmt = models.CharField(max_length=1)
    use_mmsmo = models.CharField(max_length=1)
    use_intersms = models.CharField(max_length=1)
    use_report = models.CharField(max_length=1)
    use_readreply = models.CharField(max_length=1)
    smsmt_limit_count = models.IntegerField(blank=True, null=True)
    cbu_limit_count = models.IntegerField(blank=True, null=True)
    mmsmt_limit_count = models.IntegerField(blank=True, null=True)
    mntalk_enable = models.CharField(max_length=1)
    mntalk_only = models.CharField(max_length=1)
    max_sendline = models.IntegerField()
    max_reportline = models.IntegerField()
    max_smsmoline = models.IntegerField()
    max_mmsmoline = models.IntegerField()
    checkcredit = models.CharField(max_length=1, blank=True, null=True)
    exceptcredit = models.CharField(max_length=1, blank=True, null=True)
    use_mo_autoresponse = models.CharField(max_length=1)
    print_seq = models.IntegerField(blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)
    spamcheck_all = models.CharField(max_length=1)
    use_push = models.CharField(max_length=1, blank=True, null=True)
    use_mmoreport = models.CharField(max_length=1)
    use_smoreport = models.CharField(max_length=1)
    use_cbblkspam = models.CharField(max_length=1)
    use_modupchk = models.CharField(max_length=1, blank=True, null=True)
    use_recmsg = models.CharField(max_length=1)
    blk_cbform_err = models.CharField(max_length=1)
    chk_allow_callback = models.CharField(max_length=1)
    is_public_institution = models.CharField(max_length=1)
    is_adbag_clnt = models.CharField(max_length=1)
    is_convert_rgn = models.CharField(max_length=1)
    is_remove_spchar = models.CharField(max_length=1)
    use_rptfep = models.CharField(max_length=1)
    use_oldrestspec = models.CharField(max_length=1)
    use_rptrestful = models.CharField(max_length=1)
    protocol_type = models.CharField(max_length=10)
    use_cbblkbuss_spam = models.CharField(max_length=1)
    use_ctl_itutype_cb = models.CharField(max_length=1)
    chk_dup_msgkey = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'clientinfo'


class Clientsysteminfo(models.Model):
    client_code = models.CharField(max_length=8)
    pdu_version = models.CharField(max_length=16)
    emma_version = models.CharField(max_length=16)
    system_osinfo = models.CharField(max_length=64, blank=True, null=True)
    system_dbinfo = models.CharField(max_length=256, blank=True, null=True)
    system_jreinfo = models.CharField(max_length=64, blank=True, null=True)
    install_path = models.CharField(max_length=128, blank=True, null=True)
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clientsysteminfo'


class ClntAllowCallbackInfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    callback = models.CharField(max_length=25)
    allow = models.CharField(max_length=1, blank=True, null=True)
    regtime = models.DateTimeField(blank=True, null=True)
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clnt_allow_callback_info'
        unique_together = (('client_code', 'callback'),)


class ClntAllowCallbackInfo222(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    callback = models.CharField(max_length=25)
    allow = models.CharField(max_length=1, blank=True, null=True)
    regtime = models.DateTimeField(blank=True, null=True)
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clnt_allow_callback_info222'
        unique_together = (('client_code', 'callback'),)


class ClntAllowMoCallbackInfo(models.Model):
    monumber = models.CharField(primary_key=True, max_length=20)
    client_code = models.CharField(max_length=8)
    allow = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clnt_allow_mo_callback_info'
        unique_together = (('monumber', 'client_code'),)


class ClntExceptionalCallbackInfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    callback = models.CharField(max_length=25)
    allow = models.CharField(max_length=1, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)
    expiredate = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clnt_exceptional_callback_info'
        unique_together = (('client_code', 'callback'),)


class Clntrtinfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    pdutype = models.IntegerField()
    msgtype = models.SmallIntegerField()
    priority = models.CharField(max_length=8)
    country_code = models.CharField(db_column='COUNTRY_CODE', max_length=4)  # Field name made lowercase.
    rtg_id = models.CharField(max_length=16)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clntrtinfo'
        unique_together = (('client_code', 'pdutype', 'msgtype', 'priority', 'country_code'),)


class Commoncode(models.Model):
    lcode = models.CharField(primary_key=True, max_length=4)
    scode = models.CharField(max_length=5)
    name = models.CharField(max_length=80)
    pname = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commoncode'
        unique_together = (('lcode', 'scode'),)


class Connectioninfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    server_code = models.CharField(max_length=4)
    client_id = models.CharField(max_length=20)
    allow = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connectioninfo'
        unique_together = (('client_code', 'server_code'),)

"""
class Countrycode(models.Model):
    country_code = models.CharField(primary_key=True, max_length=4)
    country_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'countrycode'
"""


class CountrycodeRuleInfo(models.Model):
    country_code = models.CharField(primary_key=True, max_length=8)
    prefix = models.CharField(max_length=8)
    min = models.IntegerField()
    max = models.IntegerField()
    regdate = models.DateTimeField(blank=True, null=True)
    regperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countrycode_rule_info'
        unique_together = (('country_code', 'prefix'),)


class CountrycodeRuleInfo3(models.Model):
    country_code = models.CharField(primary_key=True, max_length=8)
    prefix = models.CharField(max_length=8)
    min = models.IntegerField()
    max = models.IntegerField()
    regdate = models.DateTimeField()
    regperson = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'countrycode_rule_info3'
        unique_together = (('country_code', 'prefix'),)


class CountrycodeRuleInfo2(models.Model):
    country_code = models.CharField(primary_key=True, max_length=8)
    prefix = models.CharField(max_length=8)
    min = models.IntegerField()
    max = models.IntegerField()
    regdate = models.DateTimeField(blank=True, null=True)
    regperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countrycode_rule_info_2'
        unique_together = (('country_code', 'prefix'),)


class EtcCarrierInfo(models.Model):
    prefix = models.CharField(primary_key=True, max_length=8)
    carrier = models.IntegerField()
    valid = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etc_carrier_info'


class EtcCarrierInfo2(models.Model):
    prefix = models.CharField(primary_key=True, max_length=8)
    carrier = models.IntegerField()
    valid = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etc_carrier_info2'


class FaulttypeMsg(models.Model):
    fault_type = models.IntegerField(primary_key=True)
    type_message = models.CharField(max_length=20, blank=True, null=True)
    value_message = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faulttype_msg'


class GlobalDefaultMsgRuleInfo(models.Model):
    country_code = models.CharField(primary_key=True, max_length=4)
    ts_code = models.IntegerField()
    sender_id = models.CharField(max_length=64, blank=True, null=True)
    msg_header = models.CharField(max_length=128, blank=True, null=True)
    msg_hd_pattern = models.CharField(max_length=16, blank=True, null=True)
    extension_number = models.CharField(max_length=10, blank=True, null=True)
    sender_id_type = models.CharField(max_length=1)
    allow = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'global_default_msg_rule_info'
        unique_together = (('country_code', 'ts_code'),)


class GlobalMsgGroupInfo(models.Model):
    msg_group_code = models.CharField(primary_key=True, max_length=10)
    client_code = models.CharField(max_length=8)
    allow = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'global_msg_group_info'
        unique_together = (('msg_group_code', 'client_code'),)


class GlobalMsgRuleInfo(models.Model):
    country_code = models.CharField(primary_key=True, max_length=4)
    ts_code = models.IntegerField()
    msg_client_code = models.CharField(max_length=8)
    client_type = models.CharField(max_length=1)
    client_sub_id = models.CharField(max_length=16)
    sender_id = models.CharField(max_length=64, blank=True, null=True)
    msg_header = models.CharField(max_length=128, blank=True, null=True)
    extension_number = models.CharField(max_length=10, blank=True, null=True)
    allow = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'global_msg_rule_info'
        unique_together = (('country_code', 'ts_code', 'msg_client_code', 'client_sub_id'),)


class GlobalMsgRuleInfo2(models.Model):
    country_code = models.CharField(max_length=4)
    ts_code = models.IntegerField()
    msg_client_code = models.CharField(max_length=8)
    client_type = models.CharField(max_length=1)
    client_sub_id = models.CharField(max_length=16, blank=True, null=True)
    sender_id = models.CharField(max_length=64, blank=True, null=True)
    msg_header = models.CharField(max_length=128, blank=True, null=True)
    extension_number = models.CharField(max_length=10, blank=True, null=True)
    allow = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'global_msg_rule_info_2'


class GlobalMsgRuleInfoBk(models.Model):
    country_code = models.CharField(primary_key=True, max_length=4)
    ts_code = models.IntegerField()
    msg_client_code = models.CharField(max_length=8)
    client_type = models.CharField(max_length=1)
    client_sub_id = models.CharField(max_length=16)
    sender_id = models.CharField(max_length=64, blank=True, null=True)
    msg_header = models.CharField(max_length=128, blank=True, null=True)
    extension_number = models.CharField(max_length=10, blank=True, null=True)
    allow = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'global_msg_rule_info_bk'
        unique_together = (('country_code', 'ts_code', 'msg_client_code', 'client_sub_id'),)


class Groupcreditinfo(models.Model):
    group_code = models.CharField(primary_key=True, max_length=8)
    credit_period = models.SmallIntegerField()
    pdutype = models.IntegerField()
    allow = models.CharField(max_length=1, blank=True, null=True)
    resetcredit = models.CharField(max_length=1, blank=True, null=True)
    resetcredit_date = models.SmallIntegerField()
    givingcredit = models.IntegerField()
    extracredit = models.IntegerField()
    exceed_block = models.CharField(max_length=1, blank=True, null=True)
    exceed_alarm = models.CharField(max_length=1, blank=True, null=True)
    print_seq = models.IntegerField(blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)
    last_deductingtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'groupcreditinfo'
        unique_together = (('group_code', 'credit_period', 'pdutype'),)


class Gwinfo(models.Model):
    server_code = models.CharField(primary_key=True, max_length=4)
    server_name = models.CharField(max_length=20)
    server_type = models.CharField(max_length=1)
    publickey = models.TextField()
    privatekey = models.TextField()
    server_host = models.CharField(max_length=30)
    listen_port = models.SmallIntegerField()
    report_port = models.SmallIntegerField()
    smsmo_port = models.SmallIntegerField()
    mmsmo_port = models.SmallIntegerField()
    status_port = models.SmallIntegerField()
    block_port = models.SmallIntegerField()
    chk_blk = models.CharField(max_length=1, blank=True, null=True)
    allow = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwinfo'


class MoAutoResponse(models.Model):
    monumber = models.CharField(primary_key=True, max_length=20)
    chk_interval = models.IntegerField()
    message = models.TextField()
    callback = models.CharField(max_length=25, blank=True, null=True)
    starttime = models.CharField(max_length=4, blank=True, null=True)
    endtime = models.CharField(max_length=4, blank=True, null=True)
    valid = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mo_auto_response'


class Moinfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    monumber = models.CharField(max_length=20)
    country_code = models.CharField(max_length=8)
    mo_callback = models.CharField(max_length=32, blank=True, null=True)
    allow = models.CharField(max_length=1)
    transcoding = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moinfo'
        unique_together = (('client_code', 'monumber', 'country_code'),)


class Moinfo2(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    monumber = models.CharField(max_length=20)
    allow = models.CharField(max_length=1)
    transcoding = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moinfo2'
        unique_together = (('client_code', 'monumber'),)


class Msgtypeinfo(models.Model):
    msg_code = models.CharField(primary_key=True, max_length=4)
    msg_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'msgtypeinfo'


class Pushclientinfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    use_apns = models.CharField(max_length=1)
    use_c2dm = models.CharField(max_length=1)
    use_gcm = models.CharField(max_length=1)
    use_mpush = models.CharField(max_length=1)
    use_contents = models.CharField(max_length=1)
    use_file = models.CharField(max_length=1)
    use_apprun_info = models.CharField(max_length=1)
    use_location_info = models.CharField(max_length=1)
    use_push_report = models.CharField(max_length=1)
    push_limit_count = models.IntegerField()
    max_sendline = models.IntegerField()
    max_reportline = models.IntegerField()
    push_checkcredit = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pushclientinfo'


class Quethreshold(models.Model):
    seq = models.AutoField(primary_key=True)
    quetype = models.IntegerField()
    threshold_cnt = models.IntegerField()
    alert_id = models.CharField(max_length=20)
    quekind = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'quethreshold'
        unique_together = (('quetype', 'alert_id', 'quekind'),)


class Quetypeinfo(models.Model):
    quetype = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quetypeinfo'


class RemoveSpcharList(models.Model):
    remove_char = models.CharField(primary_key=True, max_length=1)
    allow = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remove_spchar_list'


class Resetcreditlog(models.Model):
    group_code = models.CharField(max_length=8)
    client_code = models.CharField(max_length=8, blank=True, null=True)
    credit_period = models.SmallIntegerField()
    pdutype = models.IntegerField()
    resettime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'resetcreditlog'


class RestfulClient(models.Model):
    client_code = models.CharField(max_length=20)
    client_report_ip = models.CharField(primary_key=True, max_length=255)
    client_report_port = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'restful_client'
        unique_together = (('client_report_ip', 'client_report_port', 'client_code'),)


class RotaryGrupNumberInfo(models.Model):
    prefix = models.CharField(primary_key=True, max_length=4)
    valid = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rotary_grup_number_info'


class Rtgroupinfo(models.Model):
    rtg_id = models.CharField(primary_key=True, max_length=16)
    pdutype = models.IntegerField()
    rtg_name = models.CharField(max_length=64, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtgroupinfo'
        unique_together = (('rtg_id', 'pdutype'),)


class Rtruleinfo(models.Model):
    tz_code = models.CharField(primary_key=True, max_length=16)
    rtg_id = models.CharField(max_length=16)
    pdutype = models.IntegerField()
    ts_code = models.IntegerField()
    valid = models.CharField(max_length=1)
    rtrule_id = models.CharField(max_length=16)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtruleinfo'
        unique_together = (('tz_code', 'rtg_id', 'pdutype', 'ts_code', 'valid'),)


class Rtruleinfo050(models.Model):
    tz_code = models.CharField(primary_key=True, max_length=16)
    rtg_id = models.CharField(max_length=16)
    pdutype = models.IntegerField()
    ts_code = models.IntegerField()
    valid = models.CharField(max_length=1)
    rtrule_id = models.CharField(max_length=16)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtruleinfo_050'
        unique_together = (('tz_code', 'rtg_id', 'pdutype', 'ts_code', 'valid'),)


class Rttimezoneinfo(models.Model):
    tz_code = models.CharField(primary_key=True, max_length=16)
    pdutype = models.IntegerField()
    starttime = models.CharField(max_length=4)
    endtime = models.CharField(max_length=4)
    memo = models.CharField(max_length=128, blank=True, null=True)
    valid = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rttimezoneinfo'
        unique_together = (('tz_code', 'pdutype'),)


class Spaminfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    spam_seq = models.IntegerField()
    allow = models.CharField(max_length=1)
    pdutype = models.IntegerField()
    spam_checktype = models.CharField(max_length=1)
    spam_contents = models.CharField(max_length=45, blank=True, null=True)
    spam_send = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spaminfo'
        unique_together = (('client_code', 'spam_seq'),)


class Spaminfo2(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    spam_seq = models.IntegerField()
    allow = models.CharField(max_length=1)
    pdutype = models.IntegerField()
    spam_checktype = models.CharField(max_length=1)
    spam_contents = models.CharField(max_length=45, blank=True, null=True)
    spam_send = models.CharField(max_length=1)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spaminfo2'
        unique_together = (('client_code', 'spam_seq'),)


class SpecialNumberInfo(models.Model):
    number = models.CharField(max_length=20)
    client_code = models.CharField(primary_key=True, max_length=8)
    valid = models.CharField(max_length=1, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_number_info'
        unique_together = (('client_code', 'number'),)


class SpecialNumberInfo33(models.Model):
    number = models.CharField(primary_key=True, max_length=20)
    valid = models.CharField(max_length=1, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_number_info_33'


class Transcodinginfo(models.Model):
    client_code = models.CharField(primary_key=True, max_length=8)
    monumber = models.CharField(max_length=20)
    output_format = models.CharField(max_length=20)
    thumbnail_cnt = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    keepratio = models.CharField(max_length=1, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transcodinginfo'
        unique_together = (('client_code', 'monumber', 'output_format'),)


class Tsgroupinfo(models.Model):
    tsg_id = models.CharField(primary_key=True, max_length=16)
    tsg_name = models.CharField(max_length=64)
    pdutype = models.IntegerField()
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsgroupinfo'
        unique_together = (('tsg_id', 'tsg_name'),)


class Tsinfo(models.Model):
    ts_code = models.IntegerField(primary_key=True)
    ts_net = models.IntegerField()
    tsg_id = models.CharField(max_length=16)
    ts_id = models.CharField(max_length=16)
    recvip = models.CharField(max_length=16)
    recvport = models.IntegerField()
    is_relay_tel = models.CharField(max_length=1)
    comment = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsinfo'


class Tsinfo050(models.Model):
    ts_code = models.IntegerField(primary_key=True)
    ts_net = models.IntegerField()
    tsg_id = models.CharField(max_length=16)
    ts_id = models.CharField(max_length=16)
    recvip = models.CharField(max_length=16)
    recvport = models.IntegerField()
    is_relay_tel = models.CharField(max_length=1)
    comment = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsinfo_050'


class TsinfoGlobal(models.Model):
    ts_code = models.IntegerField(primary_key=True)
    ts_net = models.IntegerField()
    tsg_id = models.CharField(max_length=16)
    ts_id = models.CharField(max_length=16)
    recvip = models.CharField(max_length=16)
    recvport = models.IntegerField()
    is_relay_tel = models.CharField(max_length=1)
    comment = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsinfo_global'


class TsinfoK(models.Model):
    ts_code = models.IntegerField(primary_key=True)
    ts_net = models.IntegerField()
    tsg_id = models.CharField(max_length=16)
    ts_id = models.CharField(max_length=16)
    recvip = models.CharField(max_length=16)
    recvport = models.IntegerField()
    is_relay_tel = models.CharField(max_length=1)
    comment = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsinfo_k'


class Utf8Tsinfo(models.Model):
    ts_addr = models.CharField(primary_key=True, max_length=16)
    use_utf8 = models.CharField(db_column='use_UTF8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utf8tsinfo'


class WhiteWarningNuminfo(models.Model):
    callback_number = models.CharField(primary_key=True, max_length=12)
    valid = models.CharField(max_length=1)
    memo = models.CharField(max_length=255, blank=True, null=True)
    regtime = models.DateTimeField()
    regperson = models.CharField(max_length=20, blank=True, null=True)
    updatetime = models.DateTimeField()
    updateperson = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'white_warning_numinfo'
