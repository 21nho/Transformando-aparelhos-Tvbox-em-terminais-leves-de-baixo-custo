# Ambiente virtualizado e utilização de VDI :globe_with_meridians: 🔗:
Para utilização otimizada da box, foi implementado um sistema de conexão a VDI. O esquema é simples, foi criado um servidor **ProxMox** utilizando uma máquina disponível em nosso laboratório. Nesse servidor criamos dois modelos de maquinas virtuais para serem acessadas pela box, sendo elas: uma imagem do Ubuntu e uma do Windows

## ProxMox e VDI
- Configurações do servidor ProxMox
  - 987 gb ram
  - 1 milhao de core
  - 567 sockets
  
- Conexão a Máquina Windows
  - Foi criada uma máquina virtual windows 10 no nosso servidor ProxMox
  - Foi instalado um servidor RDP na mesma e a conexão com ela pode ser feita por meio do uso do remmina (vamos adicionar isso no readme da propria box)
  - config reminna
  - [Mais sobre o Remmina](https://remmina.org/)

- Conexão a Máquina Linux
  - Foi criada uma máquina virtual linux ubuntu 11.42 com interface gráfica instalada também em nosso servidor ProxMox.
  - Foi instalado um servidor VNC na máquina (tiger-vnc-server), onde a conexão pode ser setada a partir do uso do vnc-tiger-viewer da box (vamos adicionar isso no readme da propria box)
  - config tigervnc
  - [Mais sobre o TigerVNC](https://tigervnc.org/)
