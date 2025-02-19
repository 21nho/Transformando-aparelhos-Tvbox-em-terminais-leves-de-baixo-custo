# Revisão de Hardware :mag::gear:
Esta seção detalha a análise do hardware dos aparelhos TV-Box utilizados no projeto, suas especificações, e as modificações realizadas para garantir desempenho adequado como terminais leves.

### Informações Gerais
Os aparelhos TV-Box fornecidos para este projeto possuem as seguintes características:
- **Modelo**: _MXQ-Pro 4K_
  
- **Processador**: Arquitetura ARM, com um chip da família **Rockchip rk322x**, mais especificamente o modelo **rk3228A**.
  - ISA: _ARMv7-A (32-bit)_
  - Arquitetura Cortex-A7
  - Quad-core, com frequência de até 1.2 GHz
  - Mais informações sobre o [modelo do chip](https://gadgetversus.com/processor/rockchip-rk3228a-specs/)
  
- **Portas e Conectividade**:
  - 4 Entradas USB
  - 1 Entrada HDMI
  - 1 Entrada SPDIF
  - 1 Entrada AV
  - 1 Entrada para Cartão SD
  - 1 Entrada para Cabo Ethernet
    
- **Memória Flash**: Tipo _**NAND**_, o que inviabiliza a utilização de cartões SD para rodar o sistema operacional externamente. É obrigatório gravar o boot do sistema diretamente na memória interna do aparelho.

