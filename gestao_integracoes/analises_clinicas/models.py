from django.db import models


class tb_FleuryLog(models.Model):
    id_fleurylog = models.DecimalField(max_digits=38, decimal_places=0, null=False, primary_key=True)
    nr_prescricao = models.DecimalField(max_digits=38, decimal_places=0, null=True)
    ds_comando = models.CharField(max_length=200, null=True)
    dt_evento = models.DateField(null=True)
    cd_estabelecimento = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    ds_estabelecimento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ds_estabelecimento

    class Meta:
        db_table = 'TB_FLEURYLOG'
        managed = False


class tb_fleury_log_nao_integrada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ds_estabelecimento = models.CharField(max_length=100, null=True)
    ds_setor_atendimento = models.CharField(max_length=100, null=True)
    nr_prescricao = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    dt_prescricao = models.DateField(null=True)
    dt_evento = models.CharField(max_length=30, null=True)
    ds_caracteristica = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.ds_estabelecimento

    class Meta:
        db_table = 'VW_PAINEL_PRESCR_NAO_INTEGRA'
        managed = False



class tb_fleury_log_retorno_laudo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ds_estabelecimento = models.CharField(max_length=100, null=True)
    ds_setor_atendimento = models.CharField(max_length=100, null=True)
    nr_prescricao = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    nr_atendimento = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    dt_prescricao = models.DateField(null=True)
    cd_procedimento = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    ds_sigla_exame = models.CharField(max_length=20, null=True)
    nr_ficha = models.CharField(max_length=15, null=True)
    dt_integracao_envio = models.DateField(null=True)
    ds_titulo_laudo = models.CharField(max_length=200, null=True)
    status_laudo = models.CharField(max_length=20, null=True)
    dt_laudo = models.DateField(null=True)
    tempo_dif_retorno_envio_laudo = models.DateField(null=True)
    dt_evento = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.ds_estabelecimento

    class Meta:
        db_table = 'VW_FLEURY_LOG_RETORNO_LAUDO'
        managed = False
