from django.db import models

class Measurement(models.Model):
    id = models.AutoField(primary_key=True)  
    timestamp = models.IntegerField(null=True, blank=True)  
    latitude = models.FloatField() 
    longitude = models.FloatField()
    networkType = models.CharField(max_length=50) 
    signalStrengthDbm = models.IntegerField(default=100) 
    cellIdentity = models.IntegerField(null=True)  
    pinnId = models.CharField(max_length=20, blank=True, null=True)  
    lac = models.IntegerField(null=True, blank=True) 
    tac = models.IntegerField(null=True, blank=True)  
    rsrp = models.IntegerField(null=True, blank=True) 
    rsrq = models.IntegerField(null=True, blank=True) 
    
    def __str__(self):
        return f"Measurement {self.id} @ {self.timestamp}"
    
    # class Meta:
    #     db_table = 'measurement'


