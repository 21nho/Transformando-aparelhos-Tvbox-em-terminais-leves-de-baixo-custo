# Aparelhos Tv-box como terminais leves de baixo custo :package::chart_with_downwards_trend::desktop_computer:
* Nosso projeto tem como objetivo dar nova utilidade a aparelhos Tv-Box apreendidos, o intuiito é poder realizar a transformação dos mesmos em **terminais leves e de baixo custo**, que poderiam ser utilizados tanto para uso em laboratórios acadêmicos quanto para uso pessoal de alunos que necessitassem de uma unidade funcional para estudos.

*   No nosso repositório poderá ser encontrada nossa revisão a respeito do hardware que utilizamos, a metodologia aplicada e os metódos para atingir nosso objetivo que foram colocados em prática, isso tudo com base no cenário específico em que estamos inseridos. Outros arquivos com os códigos utilizados e as customizações realizadas no nosso modelo de terminal serão encontrados aqui também.

*   O material disponibilizado para pesquisa foi cedido pelo IFRN (Instituto Federal de Ciência e Tecnologia do Rio Grande do Norte). Foram cedidos aparelhos Tv-Box de modelo Mxq-pro 4k, os quais as especificações também serão descritas em nossa revisão.

# Revisão de hardware/Seleção de distribuição linux :mag::gear:

-   Inicialmente foi feita uma revisão sobre o hardware e as configurações do aparelho cedido com que estavamos trabalhando. Os aparelhos TvBox com os quais trabalhamos possuem um processador de arquitetura **ARM**, com um sistema operacional **android 7.7**.
    Como a ideia inicial seria transformar os mesmos em terminais leves e de baixo custo, o primeiro desafio seria a instalação de um sistema operacional **linux**nos mesmos.

-   Os aparelhos utilizados possuiam um chip do tipo **rockchip**, da família **rk332x**, mais especificamente um chip do tipo **rk3228A**. Os aparelhos tvbox são do modelo Mxq-4k, possuindo 4 entradas USB, 1 entrada HDMI, 1 entrada SPDIP, 1 entrada AV, 1 entrada para cartão SD e uma última para cabo ethernet. Todos possuem memória do tipo Nand, o que incapacita a possibilidade de rodar o sistema operacional por fora em um cartão SD, e tornando obrigatório gravar o boot do sistema operacional na memória.

- Foi verificado que o dissipador é muito mal colocado junto com a pasta térmica, o que pode causar alto aquecimento do processador e causar problemas de rendimento. Em breve seram citados os métodos utilizados para contornar essa situação.

- Foi escolhida como distribuição linux instalada no nosso modelo de aparelho a distribuição **ARMBIAN**, devido a compatibilidade. Foram testadas 3 imagens diferentes da distribuição **ARMBIAN**, e foi analisado que apenas imagens do modelo  **legacy** eram compátiveis para instalação em nosso hardware.
Utilizamos inicialmente imagens que já possuem interface gráfica (xfcce) para testes e visualização de desempenho, com isso conseguimos analisar que as imagens do **Armbian-legacy-2022** eram as de versão mais atualizada possível na qual a instalação pode ser realizada.

- Após analisar um desempenho abaixo do esperado com a distribuição do **Armbian-legacy-2022-xfce** optamos pela instalação de uma versão sem interface gráfica, apenas com linha de comando (**Armbian-legacy-2022-minimal**, na qual foi configurada uma interface gráfica própria utilizando o **fluxbox**.

- Os demais detalhes sobre a customização do **fluxbox** serão citados mais abaixo. Por enquanto será explicada o método de instalação e a análise da troca do dissipador do chip, além da instalação de um cooler para impedir o superaquecimento e consequentemente melhorar o desempenho.

# Instalando sistema operacional na Tv-box :package::gear:
- É importante deixar claro que esse tipo de modelo do Tvbox não estava reconhecendo o pen-drive como opção de boot, todos os processos para criação do boot da nossa imagem foram realizados utilizando um cartão SD.
  
  1. É necessário instalar o **multitool.img.xz** do forúm do **Armbian** no cartão SD (no nosso caso em específico ao extrair o arquivo ele costumava corromper ou apresentar erro utilizando o comando **unxz** ou outros erros com outros softwares de criação de boot, portanto utilizamos o software **Balena Etcher** para criar o boot.
     
  2. Com o Tvbox ainda desligado, deve se inserir o cartão SD no mesmo e logo em seguida ligá-lo. Após isso ele irá iniciar em uma tela de multitool opções nas quais você irá selecionar a opção 1 (criar backup do android). Esta etapa é importante pois após o backup será gerado um arquivo dentro das pastas do boot do SD, e o tamanho da pasta **images** irá poder receber arquivos maiores alocados, permitindo agora que seja possível jogar nossa imagem **Arbiam-legacy-2022-minimal.img**. Após o backup finalizar basta dar um shutdown e voltar a configurar o cartão SD no computador.
     
  3. Configurando agora o cartão SD, basta apenas mover a imagem do **Armbian** escolhida para dentro do diretório **images** do cartão SD. Após isso ter sido feito basta novamente iniciar o aparelho Tvbox com o cartão SD inserido.
     
  4. Ao iniciar a tela de multitool opções você irá selecionar a opção **''install Armbian via-Step Nand''** e selecionar a memoria disponível. Logo em seguida basta escolher a imagem do **Armbian** que você instalou e dar um burn, após esse processo ser concluído basta dar um **shutdown** na máquina.
     
  5. Inicie o Aparelho sem o cartão SD, após esse processo ele já irá iniciar com o boot do linux pronto.
 
# Código de autenticação na rede do ifrn :key::white_check_mark:

- Para poder autenticar nossas máquinas Tvbox com linux recém instalado foi criado um código em python que permite a autenticação do usuário com base no certificado da eduroam, utilizando matrícula e senha do suap para autenticação. Basta utilizar o código **auth-ifrn.py**, obtendo-o via **scp** ao possuir seu Tvbox conectado em outro aparelho no mesmo barramento (lembrando que é um código adaptado com base na url do IFRN, mais especificamente com a do cnat).

# Ajustes a respeito da temperatura do processador :desktop_computer::fire:
