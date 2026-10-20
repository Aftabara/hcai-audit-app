import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="HCAI Governance & Auditing Platform",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Header
st.title("⚖️ Human-Centred AI Governance & Auditing Platform (HCAI-GAP)")
st.markdown("""
**Operationalizing the 4-Cluster HCAI Framework for Q1 Research & Regulatory Compliance**  
*Translating Ethics, Governance, Inclusive Design, and Technical Security into Actionable Auditing Engine.*
""")

st.divider()

# Sidebar: System Metadata
st.sidebar.header("📋 AI System Profile")
system_name = st.sidebar.text_input("System / Project Name", "Clinical Triage LLM Agent")
organization = st.sidebar.text_input("Deploying Organization", "HealthTech Innovations Ltd.")
domain = st.sidebar.selectbox("Application Domain", ["Healthcare & Medicine", "Finance & Lending", "Public Administration", "Education", "Autonomous Systems / Transport", "Customer Operations", "Other"])
model_type = st.sidebar.selectbox("Model Architecture", ["Generative AI / LLM Agent", "Multimodal Foundation Model", "Computer Vision / Biometrics", "Tabular Classifier / Predictive ML", "Rule-Based Expert System"])
autonomy_level = st.sidebar.select_slider("System Autonomy Level", options=["Advisory (Human-in-the-Loop)", "Shared Control (Human-on-the-Loop)", "Full Autonomy (Human-out-of-the-Loop)"])

st.sidebar.divider()
st.sidebar.info("💡 **HCAI-GAP Version 1.0**\nBased on Web of Science Citation-Network Mapping (N = 786). Compliant with EU AI Act & IEEE P7000 Standards.")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🇪🇺 1. EU AI Act Risk Classification", 
    "📊 2. 4-Cluster Compliance Assessment", 
    "📈 3. Scorecard & Gap Analysis", 
    "📄 4. Export Audit Report"
])

# ---------------------------------------------------------
# TAB 1: EU AI ACT RISK CLASSIFICATION
# ---------------------------------------------------------
with tab1:
    st.header("EU AI Act Statutory Risk Tier Evaluator")
    st.write("Evaluate system features against the European Union AI Act risk hierarchy (Regulation EU 2024/1689).")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Article 5: Prohibited Practices Check")
        p1 = st.checkbox("Uses real-time remote biometric identification in publicly accessible spaces for law enforcement?")
        p2 = st.checkbox("Deploys subliminal techniques or cognitive behavioral manipulation causing harm?")
        p3 = st.checkbox("Executes social scoring by public or private actors leading to detrimental treatment?")
        p4 = st.checkbox("Infers emotions of natural persons in workplace or educational environments?")
        
        st.subheader("Article 6: High-Risk Category Criteria")
        h1 = st.checkbox("System operates as a safety component or product covered by EU harmonization legislation?")
        h2 = st.checkbox("Used in critical infrastructure, medical diagnostic triage, or emergency response?")
        h3 = st.checkbox("Used in educational admission, employment evaluation, or worker management?")
        h4 = st.checkbox("Used for essential private/public credit scoring, life insurance, or welfare benefits?")
        h5 = st.checkbox("Used in law enforcement, migration management, or administration of justice?")

    with col2:
        st.subheader("Article 52: General Purpose AI (GPAI) & Transparency")
        g1 = st.checkbox("Built upon or fine-tuned from General Purpose AI / Foundation LLM architectures?")
        g2 = st.checkbox("Interacts directly with natural persons (requires explicit disclosure)?")
        g3 = st.checkbox("Generates synthetic audio, image, video, or textual content (deepfake / GenAI)?")

        # Classification Engine
        if p1 or p2 or p3 or p4:
            risk_tier = "UNACCEPTABLE RISK (PROHIBITED)"
            status_color = "error"
            risk_desc = "The evaluated features trigger Article 5 prohibitions under the EU AI Act. System deployment is legally prohibited without statutory exemptions."
        elif h1 or h2 or h3 or h4 or h5:
            risk_tier = "HIGH RISK"
            status_color = "warning"
            risk_desc = "System falls under Annex I/III High-Risk classifications. Mandatory requirements apply: pre-market conformity assessment, Fundamental Rights Impact Assessment (FRIA), continuous logging, and human oversight."
        elif g1 or g2 or g3:
            risk_tier = "GENERAL PURPOSE AI / TRANSPARENCY OBLIGATION"
            status_color = "info"
            risk_desc = "System subject to GPAI transparency requirements: technical documentation disclosure, training data copyright summary, and synthetic content watermarking."
        else:
            risk_tier = "MINIMAL / LOW RISK"
            status_color = "success"
            risk_desc = "System falls into minimal risk category. Voluntary compliance with HCAI ethical codes of conduct is recommended."

        st.markdown("---")
        if status_color == "error":
            st.error(f"### Result: {risk_tier}")
        elif status_color == "warning":
            st.warning(f"### Result: {risk_tier}")
        elif status_color == "info":
            st.info(f"### Result: {risk_tier}")
        else:
            st.success(f"### Result: {risk_tier}")
        
        st.write(risk_desc)

# ---------------------------------------------------------
# TAB 2: 4-CLUSTER COMPLIANCE ASSESSMENT
# ---------------------------------------------------------
with tab2:
    st.header("4-Cluster HCAI Quantitative Assessment")
    st.write("Rate compliance across the 20 core HCAI indicators identified in the citation-network literature review.")

    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Cluster 1: Ethics & Transparency")
        e1 = st.slider("1.1 Local Explainability (XAI) & Interpretability", 0, 5, 3, help="Model provides SHAP/LIME or feature attributions for outputs")
        e2 = st.slider("1.2 Algorithmic Fairness & Demographic Parity Testing", 0, 5, 2, help="Quantitative testing for demographic disparity across sensitive groups")
        e3 = st.slider("1.3 Interactive Bias Negotiation for Stakeholders", 0, 5, 3, help="Interfaces enable human review and adjustment of fairness trade-offs")
        e4 = st.slider("1.4 User Trust Calibration & Over-reliance Prevention", 0, 5, 2, help="System explicitly communicates uncertainty and confidence bounds")
        e5 = st.slider("1.5 Ecological Sustainability & Green Compute", 0, 5, 4, help="Model training and inference carbon footprint tracking and optimization")

        st.subheader("Cluster 2: Governance & Accountability")
        g1_score = st.slider("2.1 Traceable Audit Logs & Decision Recordkeeping", 0, 5, 4, help="System records timestamped input/output parameters for auditability")
        g2_score = st.slider("2.2 Administrative Discretion Oversight", 0, 5, 3, help="Clear human appeal workflows for decisions affecting natural persons")
        g3_score = st.slider("2.3 Fundamental Rights Impact Assessment (FRIA)", 0, 5, 2, help="Formal pre-deployment evaluation of impact on civil rights and equity")
        g4_score = st.slider("2.4 Post-Market Monitoring & Incident Reporting", 0, 5, 3, help="Automated detection and logging of runtime performance degradation")
        g5_score = st.slider("2.5 Organizational Responsibility & Liability Assignment", 0, 5, 4, help="Formally designated human roles responsible for model outputs")

    with c2:
        st.subheader("Cluster 3: Inclusive Design & Value Alignment")
        i1 = st.slider("3.1 Value-Sensitive Requirements Engineering (VSD)", 0, 5, 2, help="Formal elicitation and modeling of human values during initial design")
        i2 = st.slider("3.2 Participatory Co-Creation with Diverse End-Users", 0, 5, 1, help="Marginalized communities and lay users actively engaged in co-design")
        i3 = st.slider("3.3 Accessibility Standards & Equitable Access", 0, 5, 3, help="WCAG 2.1 compliance and accommodation for non-expert users")
        i4 = st.slider("3.4 Meaningful Human Control & Override Interfaces", 0, 5, 4, help="Operators possess immediate physical/digital override switches")
        i5 = st.slider("3.5 Sociotechnical System (iSTS) Joint Optimization", 0, 5, 3, help="System evaluated across individual, workplace, and societal tiers")

        st.subheader("Cluster 4: Technical Security & System Safety")
        s1 = st.slider("4.1 Dynamic Operational Safety Limits & Bounds", 0, 5, 4, help="Control-theoretic limits preventing out-of-bounds autonomous actions")
        s2 = st.slider("4.2 Differential Privacy & Data Minimization", 0, 5, 3, help="Protections against membership inference and training data extraction")
        s3 = st.slider("4.3 Zero-Trust Cybersecurity & Adversarial Robustness", 0, 5, 3, help="Defenses against prompt injection, model poisoning, and adversarial noise")
        s4 = st.slider("4.4 Fail-Safe Redundancy & Health Diagnostics", 0, 5, 4, help="Self-diagnostics and safe fallback states during component failures")
        s5 = st.slider("4.5 Hallucination & Non-Deterministic Guardrails", 0, 5, 2, help="Real-time verification and filtering layers for generative outputs")

# Calculations
cluster1_score = (e1 + e2 + e3 + e4 + e5) / 25.0 * 100
cluster2_score = (g1_score + g2_score + g3_score + g4_score + g5_score) / 25.0 * 100
cluster3_score = (i1 + i2 + i3 + i4 + i5) / 25.0 * 100
cluster4_score = (s1 + s2 + s3 + s4 + s5) / 25.0 * 100
overall_hcai_index = (cluster1_score + cluster2_score + cluster3_score + cluster4_score) / 4.0

# ---------------------------------------------------------
# TAB 3: SCORECARD & GAP ANALYSIS
# ---------------------------------------------------------
with tab3:
    st.header("HCAI Compliance Scorecard & Gap Analysis")
    
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Overall HCAI Index", f"{overall_hcai_index:.1f}%")
    m2.metric("1. Ethics & XAI", f"{cluster1_score:.0f}%")
    m3.metric("2. Governance", f"{cluster2_score:.0f}%")
    m4.metric("3. Inclusive Design", f"{cluster3_score:.0f}%")
    m5.metric("4. Technical Security", f"{cluster4_score:.0f}%")

    st.markdown("---")
    
    col_chart, col_gaps = st.columns([1.2, 1])
    
    with col_chart:
        st.subheader("Cluster Profile (Radar Visualization)")
        
        categories = ['Ethics & XAI', 'Governance', 'Inclusive Design', 'Technical Security']
        values = [cluster1_score, cluster2_score, cluster3_score, cluster4_score]
        
        # Radar Chart
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        values_radar = values + [values[0]]
        angles += [angles[0]]
        
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, values_radar, color='#2F5496', alpha=0.35)
        ax.plot(angles, values_radar, color='#2F5496', linewidth=2.5)
        ax.set_yticklabels([20, 40, 60, 80, 100], color="grey", size=8)
        ax.set_ylim(0, 100)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontweight='bold', size=10)
        ax.set_title(f"HCAI Readiness Profile: {system_name}", pad=20, fontweight='bold')
        st.pyplot(fig)

    with col_gaps:
        st.subheader("Identified Critical Gaps & Recommendations")
        
        gaps = []
        if cluster1_score < 60:
            gaps.append("⚠️ **Ethics Gap**: Insufficient fairness testing or XAI interpretability interfaces. Implement local attributions (SHAP/LIME).")
        if cluster2_score < 60:
            gaps.append("⚠️ **Governance Gap**: Incomplete Fundamental Rights Impact Assessment (FRIA) or audit logging. Establish formal pre-market review.")
        if cluster3_score < 60:
            gaps.append("⚠️ **Inclusive Design Gap**: Deficient stakeholder co-design and value elicitation. Conduct participatory workshops with end-users.")
        if cluster4_score < 60:
            gaps.append("⚠️ **Technical Security Gap**: Non-deterministic hallucination risks or privacy bounds require verification guardrails.")
            
        if not gaps:
            st.success("✅ **High HCAI Maturity**: The evaluated system demonstrates balanced, robust alignment across all four thematic clusters.")
        else:
            for gap in gaps:
                st.warning(gap)

# ---------------------------------------------------------
# TAB 4: EXPORT AUDIT REPORT
# ---------------------------------------------------------
with tab4:
    st.header("Export Diagnostic Audit Summary")
    st.write("Generate a standardized JSON diagnostic record for submission with regulatory documentation or research appendices.")
    
    report_data = {
        "audit_timestamp": datetime.now().isoformat(),
        "system_metadata": {
            "name": system_name,
            "organization": organization,
            "domain": domain,
            "model_type": model_type,
            "autonomy_level": autonomy_level
        },
        "eu_ai_act_classification": {
            "risk_tier": risk_tier,
            "description": risk_desc
        },
        "hcai_quantitative_scores": {
            "overall_index": round(overall_hcai_index, 2),
            "cluster_1_ethics_xai": round(cluster1_score, 2),
            "cluster_2_governance": round(cluster2_score, 2),
            "cluster_3_inclusive_design": round(cluster3_score, 2),
            "cluster_4_technical_security": round(cluster4_score, 2)
        },
        "identified_gaps": gaps
    }
    
    json_string = json.dumps(report_data, indent=2)
    st.code(json_string, language="json")
    
    st.download_button(
        label="📥 Download Diagnostic JSON Audit File",
        data=json_string,
        file_name=f"HCAI_Audit_{system_name.replace(' ', '_')}.json",
        mime="application/json"
    )
