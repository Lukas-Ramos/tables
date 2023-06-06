import pandas as pd


patrimonio =[12398078, 12398079, 12398080, 12398081, 12398082, 12398083, 12398084, 12398085, 12398086, 12398087, 12398088, 12398089, 12398090, 12398091, 12398092, 12398093, 12398094, 12398095, 12398096, 12398097, 12398098, 12398099, 12398100, 12398101, 12398102, 12398103, 12398104, 12398105, 12398106, 12398107, 12398108, 12398109, 12398110, 12398111, 12398112, 12398113, 12398114, 12398115, 12398116, 12398117, 12398118, 12398119, 12398120, 12398121, 12398122, 12398123, 12398124, 12398125, 12398126, 12398127]
titulo = ['A Sabedoria do Bibliotecário', 'Design Thinking: na educação presencial, à distância e corporativa', 'Direito Tributário: Teoria e Prática', 'Conversas Difíceis', 'Economia Brasileira Contemporânea', 'Empresas Estatais: O regime jurídico das empresas públicas e sociedades de economia mista', 'Equilíbrio contratual e dever de renegociar', 'User Experience Design: Como criar produtos digitais com foco nas pessoas', 'A ascenção do dinheiro: A história financeira do mundo', 'Correspondência intelectual: 1949,2004', 'Contabilidade Pública: uma abordagem da administração pública', 'Valsa Brasileira', 'Entre Hidra e Hércules', 'A Marcha da Insensatez: De Troia ao Vietnã', 'Criptoativos, Tokenização, Blockchain e Metaverso: Aspectos filosóficos, Tecnológicos, Jurídicos e Econômicos', 'Crash: Uma breve história da economia', 'PIS e COFINS: Volume 2: Coleção Curso de Tributos Indiretos', 'Licitação de Registro de Preços: Comentários ao Decreto nº 7.892, de 23 de janeiro de 2013, alterado...', 'Nova lei de licitações e contratos administrativos', 'Tratado De Direito Administrativo: Vol. 7, Controle da Administração Pública e Responsabilidade do Estado', 'Tratado De Direito Administrativo: Vol. 4,Funções Administrativas Do Estado', 'Auditoria, Contabilidade e Controle Interno no Setor Público', 'Compliance nas Contratações Públicas: Exigência e Critérios Normativos', 'Contas governamentais e responsabilidade fiscal', 'Comentários às Súmulas Tributárias do STF, STJ, TRFS e CARF', 'Valuation', 'Contratos Administrativos: Manual para Gestores e Fiscais', 'Curso De Finanças Públicas: Uma Abordagem Contemporânea', 'Contabilidade de custos', 'Breve História de Quase Tudo', 'Blockchain Revolution(Português)', 'Nova lei de licitações e contratos administrativos/ Exemplar 2', 'A Startup enxuta', 'Scrum: a Arte de Fazer o Dobro do Trabalho na Metade do Tempo', 'Sapiens: uma breve história da humanidade', 'Constituição E Código Tributário Comentados: sob a ótica da Fazenda Nacional', 'Manual da Nova Lei de Licitações,Lei n.º 14.133/2021', 'Manual da Nova Lei de Licitações,Lei n.º 14.133/2021 / Exemplar 2', 'Pis e Cofins na Teoria e na Pratica: uma Abordagem Completa dos Regimes Cumulativo e Nao Cumulativo', 'PIS Cofins: Não Cumulatividade e Regimes de Incidência', 'Planejamento e Gestão Estratégica', 'Planejamento e Alinhamento Estratégico de Projetos', 'Planejamento Tributário & Incentivos Fiscais Empresariais', 'Planejamentos Tributários: limites e Restrições da Liberdade nos Planejamentos...', 'Por que as Nações Fracassam:as origens do poder, da prosperidade e da pobreza', 'Python Fluente: Programação Clara, Concisa e Eficaz', 'Manual de Planejamento Estratégico: Ferramentas Para Desenvolver, Executar e Aplicar', 'Microsoft Power BI: Gráficos, Banco de Dados e Configuração de Relatórios', 'Planejamento Estratégico: Conceitos Metodologia Práticas', 'Metodologias inovativas: Na educação presencial, a distância e corporativa']
autor = ['Michel Melot', 'Andrea Filatro', 'Carolina Costa Cavalcanti', 'Francisco Leite Duarte', 'Douglas Stone', 'Bruce Patton e Sheila Heen', 'Fabio Giambiagi', 'Alexandre Santos de Aragão', 'Anderson Schreiber', 'Rogério Pereira', 'Niall Ferguson', 'Furtado', 'Celso. ORG. Rosa Freire D. Aguiar POSF. Luiz Felipe de Alencastro', 'Roberto Bocaccio Piscitelli e Maria Zulene Farias Timbó', 'Laura Carvalho', 'Marcelo Neves', 'Barbara W. Tuchman', 'Agostinho Gomes Cascardo Junior e outros', 'Alexandre Versignassi', 'Adolpho Bergamini', 'Sidney Bittencourt', 'Reinaldo Couto', 'José Santos Carvalho Filho; Fernando D. M. Almeida', 'Floriano De Azevedo Marques Neto e Aline Lícia Klein', 'Domingos Poubel de Castro', 'Rodrigo Pironti Aguirre de Castro e Mirela M. Ziliotto', 'Luiz Henrique Lima', 'Eduardo Domingos Bottallo e José Eduardo S. de Melo', 'Aswaty Damodaran', 'Gabriela Verona Pércio', 'Edilberto Carlos Pontes Lima', 'Silvio Aparecido Crepaldi e Guilherme Simões Crepaldi', 'Bill Bryson', 'Don Tapscott e Alex Tapscott', 'Reinaldo Couto', 'Eric Ries', 'Jeff Sutherland e J.J. Sutherland', 'Yuval Noah Harari', 'Claudio Seefelder e Rogério Campos', 'Levi Rodrigues Vaz', 'Levi Rodrigues Vaz', 'Adolpho Bergamini e Marcelo M. Peixoto, Coords', 'Solon Sehn', 'Felipe Decourt, Hamilton da Rocha Neves e Paulo R. Baldner', 'Adilson Pize', 'José Carlos Carota', 'Carlos André Soares Nogueira', 'Daron Acemoglu, James A Robinson', 'Luciano Ramalho', 'Tadeu Cruz', 'Adalberto Fraga', 'Djalma de Pinho Rebouças de Oliveira']
edicao = [1,1,4,1,3,2,2,1,3,1,14,1,3,6,1,1,2,6,1,3,3,7,2,1,2,1,3,1,7,1,1,1,1,1,1,1,1,1,5,3,1,1,2,1,1,1,1,1,35]
ano = [2020, 2017, 2022, 2021, 2016, 2018, 2020, 2018, 2020, 2021, 2019, 2018, 2019, 2012, 2022, 2019, 2022, 2021, 2021, 2022, 2022, 2018, 2021, 2017, 2011, 2012, 2020, 2015, 2017, 2005, 2017, 2021, 2019, 2019, 2020, 2020, 2022, 2022, 2022, 2022, 2012, 2017, 2023, 2019, 2022, 2015, 2017, 2019, 2023, 2023]
dados = list(zip(patrimonio, titulo, autor, edicao, ano))
df = pd.DataFrame(data = dados)


df.columns = ['Patriomonio', 'Titulo', 'Autor', 'Edicao', 'Ano']

#1) Apresente em tela (output) toda a base de dados
display(df)

#2) Apresente o tamanho do seu dataframe (quantas colunas x linhas).
print("Tamanho do DataFrame:", df.shape)

#3) Acesse a linha (x) e apresente em tela todas as características do item.                                                 
titulo = 2
print(df.loc[titulo])

#4) Verifique se o dataframe está vazio. 
if df.empty:
    print("O DataFrame está vazio.")
else:
    print("O DataFrame não está vazio.")

#5) Apresente em tela os 5 primeiros registros da base de dados.
print(df.head())

#6) Exclua um item (linha) de sua de sua base de dados.
edicao = 3  
df = df.drop(edicao)
print("Item excluído. Novo DataFrame:")
display(df)

#7) Adicione um item (linha) na sua base de dados
novo_item = [12398128, 'Monstro do pantano', 'Alan Moore', 6, 2003] 
df = df.append(pd.Series(novo_item, index=df.columns), ignore_index=True)
print("Item adicionado. Novo DataFrame:")
display(df) 

#8) Transponha a coluna para a linha em sua base de dados
df_transposto = df.transpose()
print("DataFrame transposto:")
display(df_transposto)

#9) Apresente em tela somente a 1a e a 2a coluna (rótulo) da base de dados
colunas_selecionadas = ['Patriomonio', 'Titulo']  
df_selecionado = df[colunas_selecionadas]
print("Primeira e segunda coluna da base de dados:")
display(df_selecionado)