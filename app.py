import streamlit as st
import requests

def fetch_conversion_factor(source, target):
    url = f"https://free.currconv.com/api/v7/convert?q={source}_{target}&compact=ultra&apiKey=9aa0c54f5ad4c460c36d"
    response = requests.get(url)
    response = response.json()
    return response[f'{source}_{target}']

def main():
    st.title("Currency Converter")
    
    source_currency = st.text_input("Enter source currency (e.g., USD):")
    target_currency = st.text_input("Enter target currency (e.g., EUR):")
    amount = st.number_input("Enter amount:", min_value=0.0)

    if st.button("Convert"):
        if source_currency and target_currency and amount:
            conversion_factor = fetch_conversion_factor(source_currency, target_currency)
            final_amount = round(amount * conversion_factor, 2)
            st.write(f"{amount} {source_currency} is {final_amount} {target_currency}")
        else:
            st.write("Please fill all fields.")

if __name__ == "__main__":
    main()
