# REVISÃO DE HARDWARE E COMPATIBILIDADE DE DISTRIBUIÇÕES LINUX 

- Inicialmente foi feita uma revisão sobre o hardware e as configurações do aparelho cedido com que estavamos trabalhando. Os aparelhos TvBox com os quais trabalhamos possuem um processador de arquitetura **ARM**, com um sistema operacional **android 7.7**.
  Como a ideia inicial seria transformar os mesmos em terminais leves e de baixo custo, o primeiro desafio seria a instalação de um sistema operacional **linux**nos mesmos.

- Os aparelhos utilizados possuiam um chip do tipo **rockchip**, da família **rk332x**, mais especificamente um chip do tipo **rk3228A**. Os aparelhos tvbox são do modelo Mxq-4k, possuindo 4 entradas USB, 1 entrada HDMI, 1 entrada SPDIP, 1 entrada AV, 1 entrada para cartão SD e uma última para cabo ethernet.

- Foi escolhida como distribuição linux que seria instalada no nosso modelo de aparelho a distribuição **ARMBIAN**, devido a compatibilidade com o modelo de chip. Foram testadas 3 imagens diferentes da distribuição **ARMBIAN**, e foi analisado que apenas imagens do modelo **legacy** e **minimal** eram compátiveis para instalação em nosso hardware.
Utilizamos inicialmente imagens que já possuem interface gráfica para testes e visualização de desempenho perantes hardware, com isso conseguimos analisar que as imagens do **Armbian-legacy-2022**
