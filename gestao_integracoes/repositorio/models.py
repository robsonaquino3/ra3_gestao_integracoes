from django.db import models

class vw_mapa_integracoes(models.Model):
    id = models.DecimalField(max_digits=20, decimal_places=0, primary_key=True)
    ds_unidade = models.CharField(max_length=150, null=True)
    ds_uf = models.CharField(max_length=2, null=True)
    ds_sistema = models.CharField(max_length=30, null=True)
    ds_processo = models.CharField(max_length=50, null=True)
    ds_processos_negocio = models.CharField(max_length=150, null=True)
    qt_processo = models.CharField(max_length=10, null=True)
    qt_servico = models.CharField(max_length=10, null=True)
    qt_banco = models.CharField(max_length=10, null=True)
    qt_arquivo = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.ds_unidade

    class Meta:
        db_table = 'vw_mapa_integracoes'
        managed = False