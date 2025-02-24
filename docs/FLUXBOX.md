# Customização do Fluxbox 🎨🖌️
  Devido as limitações de hardware, foi criada uma customização do próprio ambiente gráfico utilizando o WindowManager **[FluxBox](https://fluxbox.org/)**. As customizações transformaram um ambiente totalmente CLI em um ambiente gráfico ideal para usuários não familiarizados com sistemas Linux.
  
## Instalação de Pacotes e Ambiente Gráfico
  - Segue a instalação de vários pacotes que virão a ser utilizados nos scripts armazenados neste repositório que são necessários para a configuração do ambiente funcionar
 ```py
  apt install xorg fluxbox xinit xterm feh pcmanfm zenith
  ```
  - _**xorg**: servidor gráfico._
  - _**fluxbox**: gerenciador de janelas minimalista._
  - _**xinit**: iniciar a sessão gráfica manualmente._
  - _**xterm**: terminal simples para interagir com o sistema._
  - _**feh**: visualizador de imagens e configurador de fundo de tela._
  - _**pcmanfm**: gerenciador de arquivos._
  - _**zenith**: interface de terminal para monitoramento de sistema._ 

  
## Aplicações
```py
  apt install wireshark featherpad midori luakit
  ```
  - _**Wireshark**: ferramenta de captura e análise de pacotes de rede._

    ![image alt](https://github.com/21nho/Transformando-aparelhos-Tvbox-em-terminais-leves-de-baixo-custo/blob/4b948f018e250087180b0cc9398c3100ac7745a5/docs/wireshark.png)
    
  - _**Featherpad**: editor de texto leve e funcional._

    ![image alt](https://github.com/21nho/Transformando-aparelhos-Tvbox-em-terminais-leves-de-baixo-custo/blob/ddaec5c3b640d98f8658ee76ce2379c2ebf47b04/docs/featherpad.png)
    
  - _**Midori**: navegador web._
    ![image alt](https://github.com/21nho/Transformando-aparelhos-Tvbox-em-terminais-leves-de-baixo-custo/blob/0cd3ce52bc87b2f64e72d464e9a6dd612e45e081/docs/midori.png)
    
  - _**Luakit**: navegador web baseado em WebKitGTK, focado em usuários que preferem um controle completo sobre a interface._

## Conectividade
- Para meios de conexão de rede sem fio, foram utilizados scripts para autenticação no WiFi com método **SSID-Senha** (apresentando uma interface gráfica). O mesmo _**não funciona caso a rede necessite de algum certificado**_. Foi utilizado como base um outro [repositório](https://github.com/sh377c0d3/connect_wifi_wpa-supplicant), o qual fizemos algumas alterações nos códigos para atender nossas necessidades.
  
- Para autenticar as máquinas _TvBox_, foi criado um código em python [(auth-ifrn.py)](/scripts/auth-ifrn.py), que permite a autenticação do usuário com base no certificado da _Eduroam_, utilizando matrícula e senha do SUAP para autenticação. 

## Mudanças visuais / Conforto

- Foram customizadas teclas de atalho (_hotkeys_) no sistema _FluxBox_.
- Customização da Área de Trabalho (ícones, atalhos, plano de fundo, [read-me](readmebox.md)).
- Servidor NTP configurado para ajuste de horário.

  ![image alt](https://github.com/21nho/Transformando-aparelhos-Tvbox-em-terminais-leves-de-baixo-custo/blob/6b2cb452ff30e78f6975bb0881c7b7f2df4df41e/docs/areadetrabalho.png)
