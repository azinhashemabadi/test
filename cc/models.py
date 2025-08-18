from django.db import models

class Measurement(models.Model):
    id = models.AutoField(primary_key=True)  
    timestamp = models.BigIntegerField(null=True, blank=True) 
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

class Ping(models.Model):
    timestamp = models.BigIntegerField(null=True, blank=True) 
    host = models.CharField(max_length=1000)
    responseTimeMs = models.FloatField()
    wasSuccessful = models.BooleanField(default=False) 
    
    def __str__(self):
        return f"ping {self.id} @ {self.timestamp}"
    
class DNS(models.Model):
    timestamp = models.BigIntegerField(null=True, blank=True) 
    hostname = models.CharField(max_length=100) 
    resolvedIpAddress = models.CharField(max_length=45)
    resolutionTimeMs = models.BigIntegerField(null=True, blank=True)
    wasSuccessful = models.BooleanField(default=False, blank=True) 
    
    def __str__(self):
        return f"DNS {self.id} @ {self.timestamp}"
    
class Download(models.Model):
    timestamp = models.BigIntegerField(null=True, blank=True) 
    fileSizeInBytes = models.BigIntegerField(null=True, blank=True) 
    durationInMs = models.BigIntegerField(null=True, blank=True) 
    speedMbps = models.FloatField() 
    
    def __str__(self):
        return f"Download {self.id} @ {self.timestamp}"
    
class Upload(models.Model):
    timestamp = models.BigIntegerField(null=True, blank=True) 
    fileSizeInBytes = models.BigIntegerField(null=True, blank=True) 
    durationInMs = models.BigIntegerField(null=True, blank=True) 
    speedMbps = models.FloatField() 
    
    def __str__(self):
        return f"Upload {self.id} @ {self.timestamp}"
    
class Web(models.Model):
    timestamp = models.BigIntegerField(null=True, blank=True) 
    url = models.CharField(max_length=1000)  
    responseTimeMs = models.BigIntegerField(null=True, blank=True) 
    httpStatusCode = models.IntegerField() 
    wasSuccessful = models.BooleanField(default=False) 

    
    def __str__(self):
        return f"Download {self.id} @ {self.timestamp}"

# timestamp = models.BigIntegerField(null=True, blank=True)
