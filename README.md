# STP-Claim-Root-Bridge-Attack

**Estudiante:** Masucci Franco Rincón  
**Matrícula:** 2024-1250  
**Asignatura:** Seguridad de Redes  
**Fecha:** 13/02/2026  

**Link del video:*https://itlaedudo-my.sharepoint.com/:v:/g/personal/20241250_itla_edu_do/IQDqDMBW5A-eQalVSdPDmZXAASxAv5qU3oMLhEoZbmFfHGw*

---

### Descripción y Topología 

El laboratorio se ha desplegado en un entorno virtualizado utilizando **GNS3**, simulando una infraestructura de red corporativa vulnerada desde el interior.

### Detalles de la Topología



**Direccionamiento IP:** Subred `10.12.50.0/24`

**Atacante:** Kali Linux (00:0c:29:b7:78:45)

**Víctima:** Sw2 (root bridge) 

<img width="521" height="302" alt="image" src="https://github.com/user-attachments/assets/973f36d1-6b4f-43d8-b383-4c296712c79b" />




### Objetivo del Script
Este es script su fin es que la maquina atacante sea root bridge por su Mac-Adress es más baja que las de los switches



### Parámetros Usados

```
dst = "01:80:c2:00:00:00"              
rootid = 0                            
bridgeid = 0                           
rootmac = ATTACKER_MAC                 
bridgemac = ATTACKER_MAC               
dsap = 0x42                           
ssap = 0x42                           
ctrl = 0x03                            
time.sleep(2)  
```                     

## Evidencias de Ejecución
## 1- Sw2 siendo el Root bridge
<img width="492" height="291" alt="image" src="https://github.com/user-attachments/assets/2063ee35-7134-4c58-8bd0-4da6c096601e" />


## 2- Cambio de root bridge del Sw2 a la maquina atacante
<img width="960" height="510" alt="image" src="https://github.com/user-attachments/assets/5f7f0176-cea4-4f59-9401-91ea66f5a798" />



### Requisitos para utilizar la herramienta.
* Acceso a capa 2
* Sin autenticacion
* Scapy y python3



### Medidas de Mitigación
1.  BPDU Filter
2.  Configurar Root bridge manualmente
3.  Port Security (limitar las Macs)
4.  Monitoreo y alertas
5.  Segmentación de red
6.  Deshabilitar los puertos no usados

```bash
interface range e0/1-x
spanning-tree bpduguard enable
exit


spanning-tree portfast bpduguard default
interface gi0/1
spanning-tree guard root
