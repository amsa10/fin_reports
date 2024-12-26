from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_analysis_with_gpt2(context):
    # Load GPT-2 tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")

    # Tokenize input
    inputs = tokenizer.encode(context, return_tensors="pt", max_length=512, truncation=True)

    # Generate text
    outputs = model.generate(inputs, max_length=300, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)

    # Decode and return the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

def generate_shale_oil_report(shale_data):
    # Build stock performance text dynamically
    stock_performance = ""
    for company, data in shale_data.items():
        trend = "increased" if data["price_change"] > 0 else "decreased"
        stock_performance += (
            f"The stock price of {company} ({data['ticker']}) has {trend} by "
            f"{abs(data['price_change']):.2f}% over the past 5 days, reaching ${data['current_price']:.2f}.\n"
        )

    # Generate analysis using GPT-2
    context = (
        "Recent trends in the Shale Oil market highlight the impact of price fluctuations and production rates on profitability. "
        "Write a detailed analysis considering stock performance, energy policies, and market dynamics.\n"
        + stock_performance
    )
    analysis = generate_analysis_with_gpt2(context)

    # Combine everything into the final report
    report = f"""
    === Weekly Shale Oil Market Analysis ===

    **Stock Performance**:
    {stock_performance}

    **Analysis**:
    {analysis.strip()}
    """
    return report
