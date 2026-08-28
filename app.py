import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Laudo e Cadastro Técnico - Rede Cidadã",
    page_icon="💻",
    layout="wide"
)

# Estilização
st.markdown("""
<style>
    .main-header {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 16px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 25px;
    }
    .section-title {
        background-color: #F3F4F6;
        padding: 8px 12px;
        border-radius: 5px;
        font-weight: bold;
        color: #1F2937;
        margin-top: 15px;
        margin-bottom: 15px;
        border-left: 4px solid #1E3A8A;
    }
    .laudo-box {
        border: 1px solid #D1D5DB;
        padding: 20px;
        border-radius: 8px;
        background-color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">IMANAYA SUZANI — LAUDO E CADASTRO TÉCNICO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Formulário de Controle Patrimonial e Diagnóstico da Rede Cidadã</div>', unsafe_allow_html=True)

# Banco de dados simulado inicial
if 'db' not in st.session_state:
    st.session_state.db = pd.DataFrame([{
        "PATRIMÔNIO": "RC-001734",
        "EQUIPAMENTO": "NOTEBOOK",
        "PROPRIEDADE": "REDE CIDADÃ",
        "UNIDADE": "SEDE",
        "MARCA": "LENOVO",
        "MODELO": "IDEAPAD 320-15IKB - 80YH",
        "PROCESSADOR": "CORE I3-7020U CPU 2.30 GHz",
        "MÓDULO DE MEMÓRIA RAM": "NÃO TEM",
        "MEMÓRIA RAM INTEGRADA": "4 GB",
        "TIPO HD": "SSD",
        "ESPAÇO HD": "224 GB",
        "TELA": "15,6 POL",
        "CONDIÇÕES DA TELA": "FUNCIONANDO",
        "CONDIÇÕES DO TECLADO": "FUNCIONANDO",
        "CONDIÇÕES DA CARCAÇA": "BOA",
        "TOUCHPAD": "FUNCIONANDO",
        "CÂMERA": "FUNCIONANDO",
        "DRIVE CD": "NÃO POSSUI",
        "USB": "2",
        "REDE": "1",
        "HDMI": "1",
        "TIPO C": "POSSUI",
        "PLACA DE VÍDEO": "NÃO POSSUI",
        "BATERIA": "MUITO BOA",
        "SISTEMA OPERACIONAL": "WINDOWS 10 HOME SINGLE LANGUAGE",
        "VERSÃO": "22H2",
        "SERIAL DO WINDOWS": "NTRHT-XTHTG-GBWCG-4MTMP-HH64C",
        "OBS 1": "• Equipamento auditado e cadastrado no banco de dados de manutenção.",
        "OBS 2": "• Constatado que o Led do NUM LOCK não funciona, e a câmera não estava funcionando, a mesma foi substituída.",
        "OBS 3": "• O notebook estava com HD SATA o mesmo foi substituído pelo HD SSD de 240 GB que estava no notebook patrimônio: RC-001672"
    }])

tab1, tab2, tab3 = st.tabs(["📋 Consultar / Gerar Laudo", "➕ Cadastrar Equipamento", "🗃️ Banco de Dados Completo"])

with tab1:
    col_search, col_space = st.columns([1, 2])
    with col_search:
        patrimonio_sel = st.selectbox(
            "Selecione o Número do Patrimônio:",
            options=st.session_state.db["PATRIMÔNIO"].tolist()
        )
    
    if patrimonio_sel:
        row = st.session_state.db[st.session_state.db["PATRIMÔNIO"] == patrimonio_sel].iloc[0]
        
        st.markdown('<div class="laudo-box">', unsafe_allow_html=True)
        
        # 1. IDENTIFICAÇÃO
        st.markdown('<div class="section-title">1. IDENTIFICAÇÃO DO PATRIMÔNIO E PROPRIEDADE</div>', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Nº Patrimônio", row["PATRIMÔNIO"])
        c2.metric("Tipo Equipamento", row["EQUIPAMENTO"])
        c3.metric("Propriedade", row["PROPRIEDADE"])
        c4.metric("Unidade", row["UNIDADE"])
        
        c5, c6 = st.columns(2)
        c5.write(f"**Marca:** {row['MARCA']}")
        c6.write(f"**Modelo:** {row['MODELO']}")
        
        # 2. HARDWARE
        st.markdown('<div class="section-title">2. HARDWARE E CONFIGURAÇÃO</div>', unsafe_allow_html=True)
        h1, h2, h3, h4 = st.columns(4)
        h1.write(f"**Processador:** {row['PROCESSADOR']}")
        h2.write(f"**Módulo RAM:** {row['MÓDULO DE MEMÓRIA RAM']}")
        h3.write(f"**RAM Integrada:** {row['MEMÓRIA RAM INTEGRADA']}")
        h4.write(f"**Tipo Armazenamento:** {row['TIPO HD']}")
        
        h5, h6, h7, h8 = st.columns(4)
        h5.write(f"**Espaço Armazenamento:** {row['ESPAÇO HD']}")
        h6.write(f"**Tamanho da Tela:** {row['TELA']}")
        h7.write(f"**Drive CD/DVD:** {row['DRIVE CD']}")
        h8.write(f"**Bateria:** {row['BATERIA']}")
        
        # 3. DIAGNÓSTICO
        st.markdown('<div class="section-title">3. DIAGNÓSTICO E PERIFÉRICOS</div>', unsafe_allow_html=True)
        d1, d2, d3, d4 = st.columns(4)
        d1.write(f"**Tela:** {row['CONDIÇÕES DA TELA']}")
        d2.write(f"**Teclado:** {row['CONDIÇÕES DO TECLADO']}")
        d3.write(f"**Carcaça:** {row['CONDIÇÕES DA CARCAÇA']}")
        d4.write(f"**Touchpad:** {row['TOUCHPAD']}")
        
        d5, d6, d7, d8 = st.columns(4)
        d5.write(f"**Câmera:** {row['CÂMERA']}")
        d6.write(f"**Portas USB:** {row['USB']}")
        d7.write(f"**Rede (RJ45):** {row['REDE']}")
        d8.write(f"**HDMI:** {row['HDMI']}")
        
        # 4. SO
        st.markdown('<div class="section-title">4. SISTEMA OPERACIONAL E LICENCIAMENTO</div>', unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        s1.write(f"**Sistema Operacional:** {row['SISTEMA OPERACIONAL']}")
        s2.write(f"**Versão:** {row['VERSÃO']}")
        s3.write(f"**Serial Windows:** {row['SERIAL DO WINDOWS']}")
        
        # 5. OBSERVAÇÕES
        st.markdown('<div class="section-title">5. OBSERVAÇÕES E PARECER TÉCNICO</div>', unsafe_allow_html=True)
        st.write(row['OBS 1'])
        st.write(row['OBS 2'])
        st.write(row['OBS 3'])
        
        st.markdown("---")
        st.write("**IMANAYA SUZANI** — AUXILIAR DE SUPORTE TÉCNICO — REDE CIDADÃ")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Cadastrar Novo Equipamento")
    with st.form("cad_form"):
        f1, f2, f3, f4 = st.columns(4)
        patrimonio = f1.text_input("Nº Patrimônio*")
        equipamento = f2.text_input("Tipo Equipamento", "NOTEBOOK")
        propriedade = f3.text_input("Propriedade", "REDE CIDADÃ")
        unidade = f4.text_input("Unidade", "SEDE")
        
        f5, f6, f7 = st.columns(3)
        marca = f5.text_input("Marca")
        modelo = f6.text_input("Modelo")
        processador = f7.text_input("Processador")
        
        f8, f9, f10, f11 = st.columns(4)
        mod_ram = f8.text_input("Módulo Memória RAM", "NÃO TEM")
        ram_int = f9.text_input("RAM Integrada", "4 GB")
        tipo_hd = f10.selectbox("Tipo HD/SSD", ["SSD", "HD", "NVMe"])
        espaco_hd = f11.text_input("Espaço HD/SSD", "240 GB")
        
        f12, f13, f14 = st.columns(3)
        so = f12.text_input("Sistema Operacional", "WINDOWS 10 HOME SINGLE LANGUAGE")
        versao_so = f13.text_input("Versão SO", "22H2")
        serial = f14.text_input("Serial do Windows")
        
        obs1 = st.text_area("Observação 1")
        obs2 = st.text_area("Observação 2")
        obs3 = st.text_area("Observação 3")
        
        submitted = st.form_submit_button("Salvar no Banco de Dados")
        if submitted:
            if patrimonio:
                new_data = {
                    "PATRIMÔNIO": patrimonio, "EQUIPAMENTO": equipamento, "PROPRIEDADE": propriedade,
                    "UNIDADE": unidade, "MARCA": marca, "MODELO": modelo, "PROCESSADOR": processador,
                    "MÓDULO DE MEMÓRIA RAM": mod_ram, "MEMÓRIA RAM INTEGRADA": ram_int, "TIPO HD": tipo_hd,
                    "ESPAÇO HD": espaco_hd, "TELA": "15,6 POL", "CONDIÇÕES DA TELA": "FUNCIONANDO",
                    "CONDIÇÕES DO TECLADO": "FUNCIONANDO", "CONDIÇÕES DA CARCAÇA": "BOA",
                    "TOUCHPAD": "FUNCIONANDO", "CÂMERA": "FUNCIONANDO", "DRIVE CD": "NÃO POSSUI",
                    "USB": "2", "REDE": "1", "HDMI": "1", "TIPO C": "POSSUI", "PLACA DE VÍDEO": "NÃO POSSUI",
                    "BATERIA": "BOA", "SISTEMA OPERACIONAL": so, "VERSÃO": versao_so,
                    "SERIAL DO WINDOWS": serial, "OBS 1": obs1, "OBS 2": obs2, "OBS 3": obs3
                }
                st.session_state.db = pd.concat([st.session_state.db, pd.DataFrame([new_data])], ignore_index=True)
                st.success(f"Equipamento {patrimonio} cadastrado com sucesso!")
            else:
                st.error("Por favor, preencha o número do Patrimônio.")

with tab3:
    st.subheader("Banco de Dados Completo")
    st.dataframe(st.session_state.db, use_container_width=True)
    
    # Download do Banco atualizado em Excel
    csv = st.session_state.db.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Banco de Dados (CSV / Excel)",
        data=csv,
        file_name='BANCO_DE_DADOS_REDE_CIDADA.csv',
        mime='text/csv',
    )
