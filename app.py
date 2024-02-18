import streamlit as st

def mahindra_loan_application():
    # Setting a background color
    page_bg = '''
        <style>
            body {
                background-color: #f0f5f5;
            }
        </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)

    st.title("Mahindra Car Loan Application")

    # Collecting Personal Information
    st.header("1. Personal Information")
    name = st.text_input("Full Name:")
    aadhar_card = st.text_input("Aadhar Card Number:")
    passport = st.text_input("Passport Number:")
    voter_id = st.text_input("Voter ID Number:")

    # Collecting Address Proof
    st.header("2. Address Proof")
    address_proof_type = st.selectbox("Select Address Proof Type:", ["Aadhar Card", "Passport", "Utility Bills"])
    address_proof_number = st.text_input("Address Proof Number:")

    # Upload Address Proof Document
    address_proof_upload = st.file_uploader("Upload Address Proof Document (PDF or Image):", type=["pdf", "jpg", "png"])

    # Collecting Income Proof
    st.header("3. Income Proof")
    income_proof_type = st.selectbox("Select Income Proof Type:", ["Salary Slips", "Income Tax Returns", "Bank Statements"])
    income_proof_details = st.text_area("Income Proof Details:")

    # Upload Income Proof Document
    income_proof_upload = st.file_uploader("Upload Income Proof Document (PDF or Image):", type=["pdf", "jpg", "png"])

    # Collecting Photographs
    st.header("4. Passport Size Photographs")
    num_photographs = st.number_input("Number of Photographs:", min_value=1, value=1)

    # Upload Passport Size Photographs
    photograph_uploads = st.file_uploader("Upload Passport Size Photographs (JPG or PNG):", type=["jpg", "png"], accept_multiple_files=True)

    # Loan Application Form
    st.header("5. Loan Application Form")
    st.write("Download the loan application form [here](link-to-form)")

    # Submit Button
    if st.button("Submit Application"):
        # Process the collected information and uploaded documents (you can add your logic here)
        st.success("Application submitted successfully! Mahindra Finance will contact you shortly.")

if __name__ == "__main__":
    mahindra_loan_application()
