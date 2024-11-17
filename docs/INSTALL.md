# Instalação do Sistema Operacional :package::gear:

Esta seção fornece instruções detalhadas sobre como instalar um sistema operacional Linux nos aparelhos TV-Box utilizados no projeto, transformando-os em terminais leves.

## Seleção de Distribuição Linux
Para alcançar nosso objetivo, foi necessário substituir o sistema Android presente nos dispositivos por uma distribuição Linux compatível com a arquitetura ARM. Após testes e avaliações, optamos por utilizar a distribuição **ARMBIAN**, devido à sua compatibilidade com o hardware específico do projeto.

### Testes de Distribuição
- Foram testadas três imagens diferentes da distribuição **ARMBIAN** para determinar qual versão seria compatível com o modelo MXQ-Pro 4K.
- As imagens testadas incluíam versões com interface gráfica e sem interface gráfica.
- Apenas as imagens da linha **legacy** mostraram compatibilidade para instalação em nosso hardware. A distribuição escolhida foi a **Armbian-legacy-2022**, que é a versão mais atualizada que suportou nosso hardware.

### Escolha da Imagem
- Inicialmente, utilizamos imagens com a interface gráfica **XFCE** para testes de desempenho.
- Com base nos testes, identificamos que o desempenho da versão com XFCE estava abaixo do esperado.
- Optamos então por instalar uma versão minimalista sem interface gráfica, a **Armbian-legacy-2022-minimal**, e configuramos uma interface gráfica leve utilizando o **Fluxbox**.

Os detalhes sobre a customização da interface **Fluxbox** estão disponíveis no arquivo de [Customização do Fluxbox](FLUXBOX.md).

## Instruções de Instalação
### Pré-Requisitos
Devido à natureza do hardware do TV-Box, o dispositivo não reconhece um pen-drive como opção de boot. Portanto, todas as etapas de criação de boot foram realizadas com um cartão SD.

### Passo a Passo de Instalação

1. **Preparação do Cartão SD**
   - Baixe a imagem **multitool.img.xz** do fórum do Armbian.
   - Extraia o arquivo utilizando o software **Balena Etcher**, já que métodos alternativos como o comando `unxz` apresentaram erros frequentes durante a extração.
   - Grave a imagem no cartão SD usando o Balena Etcher.

2. **Backup do Sistema Android**
   - Com o TV-Box desligado, insira o cartão SD preparado.
   - Ligue o dispositivo, que deverá iniciar automaticamente no ambiente Multitool.
   - Selecione a opção **1 (Criar Backup do Android)**. Esta etapa é importante para garantir que um backup do sistema original seja salvo.
   - Ao concluir o backup, um arquivo será gerado nas pastas do boot do SD. O tamanho do diretório **images** será ajustado para receber arquivos maiores.
   - Com o backup concluído, desligue o TV-Box e remova o cartão SD.
   - Por fim, insira o seu cartão SD em seu computador e mova o backup para onde desejar.

3. **Copiar a Imagem Armbian**
   - No computador, copie a imagem escolhida do Armbian (**Armbian-legacy-2022-minimal.img**) para o diretório **images** do cartão SD.
   - Insira o cartão SD novamente no TV-Box e ligue o dispositivo.

5. **Instalação do Armbian**
   - Após ligar o dispositivo, no menu Multitool, selecione a opção **"install Armbian via-Step Nand"**.
   - Escolha a memória disponível no dispositivo.
   - Selecione a imagem do Armbian que foi copiada para o cartão SD e inicie o processo de gravação (burn).
   - Ao finalizar, desligue o dispositivo.

6. **Iniciar o Armbian**
   - Remova o cartão SD.
   - Ligue o dispositivo normalmente, que deverá iniciar com o Linux Armbian carregado a partir da memória interna.
