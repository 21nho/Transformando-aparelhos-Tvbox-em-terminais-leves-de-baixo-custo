# Revisão de Hardware :mag::gear:

## Revisão de Hardware
Esta seção detalha a análise do hardware dos aparelhos TV-Box utilizados no projeto, suas especificações, e as modificações realizadas para garantir desempenho adequado como terminais leves.

### Informações Gerais
Os aparelhos TV-Box fornecidos para este projeto possuem as seguintes características:
- **Modelo**: MXQ-Pro 4K
- **Processador**: Arquitetura ARM, com um chip da família **Rockchip rk332x**, mais especificamente o modelo **rk3228A**.
- **Memória RAM**: 961MB
- **Armazenamento**: 8GB
- **Sistema Operacional Original**: Android 7.7
- **Portas e Conectividade**:
  - 4 Entradas USB
  - 1 Entrada HDMI
  - 1 Entrada SPDIF
  - 1 Entrada AV
  - 1 Entrada para Cartão SD
  - 1 Entrada para Cabo Ethernet
- **Memória Flash**: Tipo **NAND**, o que inviabiliza a utilização de cartões SD para rodar o sistema operacional externamente. Dessa forma, é obrigatório gravar o boot do sistema diretamente na memória interna do aparelho.

### Desafios Identificados
1. **Instalação de Linux**: Como o objetivo era transformar os dispositivos em terminais leves, foi necessário substituir o sistema Android por um sistema operacional Linux, compatível com a arquitetura ARM.
2. **Aquecimento do Processador**: Durante a análise do hardware, foi identificado que o dissipador de calor estava mal posicionado e com aplicação deficiente de pasta térmica, resultando em possíveis problemas de superaquecimento. Métodos para solucionar esses problemas serão discutidos em [Ajustes de Temperatura](TEMPERATURA.md).
