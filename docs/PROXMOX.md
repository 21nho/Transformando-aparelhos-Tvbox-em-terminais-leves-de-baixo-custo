# Ambiente Virtualizado e Conexão VDI :globe_with_meridians: 🔗
Como alternativa para contornar as limitações físicas dos aparelhos TVBox, foi implementado um sistema de conexão à **VDI**. Para isso, utilizamos um servidor _**ProxMox**_, configurado em uma máquina disponível em nosso laboratório. Nesse servidor, criamos máquinas virtuais (_VMs_) para acesso remoto a partir dos dispositivos TVBox. Entre as VMs criadas, estão uma com a imagem do _Ubuntu_ e outra com o _Windows_, permitindo que os usuários possam acessar diferentes ambientes de trabalho diretamente através da TV Box.

## 






## _ProxMox e VDI_
- ### _**Configurações do Servidor ProxMox**_
  - _Processador: Intel Core i5-4590 (4 núcleos, 3.30 GHz)_
  - _Sistema Operacional: Linux 6.8.12-8-pve_
  - _Espaço em Disco: 65.04 GiB_
  - _Memória RAM: 4GB_


- ### **_VM Windows_**
  - _Conexão realizada por meio do software Remmina_
  - _Instalação de um servidor RDP na máquina_
       
       
  - _Conectando pelo Remmina:_
  
  -      apt install-remmina-plugin
  -     192.168.0.1:5900
  -     passwd
  - [Mais sobre o Remmina...](https://remmina.org/)


- ### **_VM Linux_**
  - Foi criada uma máquina virtual linux ubuntu 11.42 com interface gráfica instalada também em nosso servidor ProxMox.
  - Foi instalado um servidor VNC na máquina (tiger-vnc-server), onde a conexão pode ser setada a partir do uso do vnc-tiger-viewer da box (vamos adicionar isso no readme da propria box)
  - config tigervnc
  - [Mais sobre o TigerVNC...](https://tigervnc.org/)
