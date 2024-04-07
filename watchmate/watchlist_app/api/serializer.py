from rest_framework import serializers

from .. models import Watchlist,Streamplatform

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields='__all__'


class StreamplatformSerializer(serializers.ModelSerializer):
    ##showing  list of flim in each plat from by using related name
    watchlist = WatchlistSerializer(many= True,read_only=True)
    
    class Meta:
        model = Streamplatform
        fields='__all__'
