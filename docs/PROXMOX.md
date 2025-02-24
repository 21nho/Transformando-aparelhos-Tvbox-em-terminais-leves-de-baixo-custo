# Ambiente Virtualizado e Conexão VDI :globe_with_meridians: 🔗
Como alternativa para contornar as limitações físicas dos aparelhos _TvBox_, foi implementado um sistema de conexão à **VDI**. Para isso, utilizamos um servidor _**ProxMox**_, configurado em uma máquina disponível em nosso laboratório. Nesse servidor, criamos máquinas virtuais (_VMs_) para acesso remoto a partir dos dispositivos _TvBox_. Entre as VMs criadas, estão uma com a imagem do _Ubuntu_ e outra com o _Windows_, permitindo que os usuários possam acessar diferentes ambientes de trabalho diretamente através da _TvBox_.
- IMAGEM

## _ProxMox e VDI_
- ### _**Configurações do Servidor ProxMox**_
  - _Processador: Intel Core i5-4590 (4 núcleos, 3.30 GHz)_
  - _Sistema Operacional: Linux 6.8.12-8-pve_
  - _Espaço em Disco: 256GiB_
  - _Memória RAM: 4GB_


- ### **_VM Windows e Linux_**
  - _VM Windows (**Win10-Pro**) / VM Linux (**Ubuntu 24.04.2**)_ 
  - _Instalação de um servidor RDP em cada máquina virtual_
  - _Conexão realizada por meio do software [Remmina](https://remmina.org/)_  
    <BR>
   ```py
  apt install-remmina-plugin
  ```
  - _Com o Remmina instalado, o script de "Seleção de Conexão Remota" disponível em nosso repositório já pode ser utilizado_
 
  -> imagem do script usando zenith



