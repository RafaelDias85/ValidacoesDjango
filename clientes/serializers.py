from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError("O Cpf deve ter 11 dígitos")

    
    # def validate_nome (self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua números neste campo")
        
    #     return nome
    
    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError ("O RG deve ter 9 digitos")
    #     return rg
    
    # def validade_celular (self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError('O Celular deve ter 11 digitos')
    #     return celular