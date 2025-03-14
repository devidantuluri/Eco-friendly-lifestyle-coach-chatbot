from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# dataset of responses
responses = {
    # responses
    'hii':"Hello user! this is Eco-friendly lifestyle coach chatbot.How can I help you.",
    'recycling': "Recycling helps reduce waste and conserves natural resources. Make sure to separate your recyclables and check local guidelines for proper recycling practices.",
    'energy': "To save energy, try switching to energy-efficient light bulbs, unplugging devices when not in use, and using energy-efficient appliances.",
    'water': "Conserving water is crucial. Try taking shorter showers, fixing leaks, and using water-saving fixtures.",
    'electricity': "To save energy, try switching to energy-efficient light bulbs, unplugging devices when not in use, and using energy-efficient appliances.",
    'transport': "Opt for public transportation, carpooling, or cycling to reduce your carbon footprint.",
    'food': "Consider eating more plant-based meals and reducing food waste. Composting can also help reduce waste and enrich soil.",
    'carbon footprint': "To reduce your carbon footprint, consider using public transport, cycling, or walking instead of driving. Additionally, eat less meat and dairy, and use energy-efficient appliances.",
    'waste': "You can reduce waste by using reusable bags, containers, and water bottles. Avoid single-use plastics and compost organic waste.",
    'energy consumption': "Save energy at home by switching to LED bulbs, unplugging devices when not in use, using energy-efficient appliances, and improving home insulation.",
    'sustainable': "Live more sustainably by reducing your carbon footprint, saving energy, eating sustainably, reducing waste, conserving water, and supporting eco-friendly businesses.",
    'plastic': "When shopping, look for products with minimal packaging and certifications like 'organic' or 'Fair Trade'. Support local and environmentally-friendly brands.",
    'climate change': "Climate change is driven by the increase of greenhouse gases in the atmosphere due to human activities. Reduce your impact by supporting renewable energy and advocating for climate policies.",
    'transportation': "Opt for sustainable transportation by using public transit, biking, walking, carpooling, or driving an electric or hybrid vehicle.",
    'green energy': "Green energy comes from renewable sources such as solar, wind, hydro, and geothermal power. Consider installing solar panels or buying green energy from your utility provider.",
    'sustainable food': "Make sustainable food choices by eating locally sourced, seasonal produce, reducing meat consumption, and avoiding food waste. Support farmers and producers with environmentally friendly practices.",
    'ecofriendly home': "Make your home eco-friendly by using energy-efficient appliances, reducing water usage, and choosing sustainable materials for renovations. Consider installing solar panels and a rainwater collection system.",
    'plastic pollution': "Reduce plastic pollution by avoiding single-use plastics, recycling properly, and choosing products with minimal or biodegradable packaging.",
    'water pollution': "Prevent water pollution by properly disposing of chemicals, avoiding littering near water sources, and supporting clean-up efforts and water conservation initiatives.",
    'composting': "Composting helps turn food scraps and yard waste into valuable soil. Start a compost bin in your backyard or use a community composting program.",
    'zero waste': "Aim for a zero-waste lifestyle by reducing, reusing, and recycling. Avoid products with excessive packaging and opt for reusable alternatives.",
    'organic': "Choose organic products to support farming practices that reduce synthetic pesticides and fertilizers. Organic farming is better for the environment and your health.",
    'sustainable fashion': "Opt for sustainable fashion by choosing clothes made from eco-friendly materials, supporting ethical brands, and recycling or donating old garments.",
    'green building': "Green building involves using sustainable materials and practices to reduce environmental impact. Look for certifications like LEED when evaluating buildings.",
    'renewable energy': "Renewable energy sources like solar, wind, and hydro are sustainable alternatives to fossil fuels. Consider investing in renewable energy systems for your home.",
    'ecofriendly products': "When shopping, look for products made from recycled materials, have minimal environmental impact, or are certified by eco-friendly labels.",
    'energy-efficient windows': "Installing energy-efficient windows can reduce heating and cooling costs. Look for windows with high energy star ratings and proper insulation.",
    'rainwater harvesting': "Collecting rainwater for use in irrigation and other non-potable applications can reduce your reliance on municipal water supplies and save money.",
    'native plants': "Planting native species in your garden can help support local wildlife and reduce the need for water and fertilizers. Native plants are adapted to local climates.",
    'ecofriendly cleaning': "Use environmentally friendly cleaning products that are free of harsh chemicals. You can also make your own cleaners using natural ingredients like vinegar and baking soda.",
    'green transportation': "Reduce your environmental impact by choosing green transportation options like electric vehicles, car-sharing programs, or walking.",
    'energy audits': "Conducting an energy audit can help you identify ways to improve your home's energy efficiency. Look for gaps in insulation, outdated appliances, and other areas to address.",
    'ethical consumption': "Practice ethical consumption by supporting companies with strong environmental and social policies. Consider the impact of your purchases on people and the planet.",
    'sustainable gardening': "Sustainable gardening practices include using organic fertilizers, conserving water, and planting diverse crops to promote a healthy ecosystem.",
    'green spaces': "Support and protect green spaces in your community. Urban parks and natural areas provide crucial benefits for both people and wildlife.",
    'low-flow fixtures': "Install low-flow faucets, showerheads, and toilets to reduce water consumption without sacrificing performance.",
    'ecofriendly packaging': "Choose products with eco-friendly packaging, such as biodegradable or recyclable materials, to minimize waste.",
    'solar power': "Consider installing solar panels to harness renewable energy from the sun. Solar power can reduce your electricity bills and carbon footprint.",
    'wind energy': "Wind turbines convert wind energy into electricity. Support wind energy projects or consider small-scale wind turbines for your home if feasible.",
    'biodegradable products': "Biodegradable products break down naturally without leaving harmful residues. Look for items made from natural materials that decompose easily.",
    'green certifications': "Look for green certifications like Energy Star, Fair Trade, and USDA Organic when making purchasing decisions to ensure products meet environmental standards.",
    'community involvement': "Get involved in local environmental initiatives and support community projects focused on sustainability and conservation.",
    'water saving tips': "Implement water-saving tips such as turning off the tap while brushing your teeth, fixing leaks promptly, and using a broom instead of a hose to clean driveways.",
    'sustainable seafood': "Choose seafood from sustainable sources to help protect marine ecosystems. Look for certifications like MSC (Marine Stewardship Council) for responsible seafood choices.",
    'food miles': "Reduce food miles by buying locally grown produce. This helps reduce greenhouse gas emissions associated with transportation and supports local farmers.",
    'electronic waste': "Properly recycle electronic waste to prevent harmful chemicals from ending up in landfills. Use designated e-waste recycling programs for safe disposal.",
    'green investing': "Consider green investing by supporting companies and funds that prioritize environmental sustainability and renewable energy projects.",
    'ecotourism': "Practice ecotourism by choosing travel options that minimize environmental impact and support conservation efforts and local communities.",
    # Additional responses
    'biomimicry': "Biomimicry involves designing products and systems inspired by nature. It helps create solutions that are sustainable and efficient, emulating natural processes.",
    'green roofs': "Green roofs involve growing vegetation on rooftops. They help insulate buildings, manage stormwater, and improve air quality.",
    'sustainable transportation': "Sustainable transportation options include electric bikes, public transit, and walking. They help reduce emissions and promote healthier lifestyles.",
    'ecofriendly personal care': "Choose personal care products made with natural ingredients and minimal packaging. Look for certifications like 'Cruelty-Free' and 'Organic'.",
    'urban farming': "Urban farming involves growing food in city environments, such as rooftop gardens and community plots. It promotes local food production and reduces transportation emissions.",
    'energy-efficient HVAC': "Upgrade to an energy-efficient HVAC system to improve heating and cooling efficiency in your home. Look for systems with high SEER ratings.",
    'sustainable water management': "Sustainable water management practices include using greywater systems, rain gardens, and permeable pavements to manage and conserve water resources.",
    'green certifications for products': "When purchasing products, look for certifications such as Cradle to Cradle, Fair Trade, and Global Organic Textile Standard (GOTS) to ensure environmental responsibility.",
    'plant-based diet': "Adopting a plant-based diet can reduce your environmental impact by lowering greenhouse gas emissions and reducing water and land use associated with animal agriculture.",
    'ecofriendly pet care': "Use eco-friendly pet care products, such as biodegradable waste bags, natural grooming products, and sustainably sourced pet food.",
    'community-supported agriculture': "Participate in community-supported agriculture (CSA) programs to receive fresh, locally grown produce while supporting local farmers and reducing food miles.",
    'reusable alternatives': "Opt for reusable alternatives to single-use items, such as cloth diapers, stainless steel straws, and glass containers.",
    'reusable': "Opt for reusable alternatives to single-use items, such as cloth diapers, stainless steel straws, and glass containers.",
    'reuse': "Opt for reusable alternatives to single-use items, such as cloth diapers, stainless steel straws, and glass containers.",
    'sustainable home decor': "Choose home decor made from sustainable materials, such as bamboo, reclaimed wood, and organic textiles. Avoid products with toxic finishes.",
    'air': "Electric vehicles (EVs) produce zero tailpipe emissions and can help reduce your carbon footprint. Consider EVs or plug-in hybrids for a more sustainable transportation option.",
    'electric vehicles': "Electric vehicles (EVs) produce zero tailpipe emissions and can help reduce your carbon footprint. Consider EVs or plug-in hybrids for a more sustainable transportation option.",
    'energy efficient water heaters': "Upgrade to an energy-efficient water heater to reduce energy consumption and lower utility bills. Look for models with high energy factor ratings.",
    'sustainable fisheries': "Support sustainable fisheries by choosing seafood that is responsibly sourced and certified by organizations like the Marine Stewardship Council (MSC).",
    'ecofriendly travel': "When traveling, reduce your environmental impact by choosing eco-friendly accommodations, using public transportation, and minimizing waste.",
    'green office practices': "Adopt green office practices by reducing paper usage, recycling, and using energy-efficient equipment to create a more sustainable workplace.",
    'upcycling': "Upcycling involves creatively repurposing old items into new products. It reduces waste and can create unique and functional items.",
    'climate advocacy': "Advocate for climate action by supporting policies and initiatives that address climate change and promote sustainable development.",
    'sustainable packaging': "Choose products with sustainable packaging options, such as biodegradable materials or minimal packaging, to reduce waste.",
    'biomass energy': "Biomass energy is derived from organic materials like wood, agricultural residues, and food waste. It can be used for electricity and heating, and is considered a renewable energy source.",
    'ecofriendly insulation': "Use eco-friendly insulation materials, such as cellulose, sheep’s wool, or recycled denim, to improve your home's energy efficiency and reduce environmental impact.",
    'water-efficient landscaping': "Implement water-efficient landscaping techniques, such as xeriscaping, to reduce water consumption and create a sustainable garden.",
    'sustainable building materials': "Choose sustainable building materials, such as recycled steel, reclaimed wood, and low-VOC paints, to minimize the environmental impact of construction projects.",
    'green certifications for homes': "Look for green certifications like LEED, BREEAM, or ENERGY STAR when evaluating homes for their environmental performance and sustainability features.",
    'food preservation': "Practice food preservation techniques, such as canning, freezing, and fermenting, to reduce food waste and extend the shelf life of seasonal produce.",
    'natural pest control': "Use natural pest control methods, such as companion planting and beneficial insects, to manage garden pests without harmful chemicals.",
    'sustainable packaging design': "Support companies that prioritize sustainable packaging design by using materials that are recyclable, compostable, or made from recycled content.",
    'climate-resilient landscaping': "Create climate-resilient landscapes by selecting drought-tolerant plants and using sustainable practices to adapt to changing climate conditions.",
    'ecofriendly home improvements': "Make eco-friendly home improvements, such as upgrading to energy-efficient appliances, installing low-flow fixtures, and using sustainable building materials.",
    'ecofriendly hobbies': "Engage in eco-friendly hobbies, such as gardening, DIY upcycling projects, and nature conservation activities, to promote sustainability in your leisure time.",
    'sustainable waste management': "Implement sustainable waste management practices by reducing waste generation, recycling, and composting to minimize environmental impact.",
    'green business practices': "Encourage businesses to adopt green practices, such as reducing energy consumption, minimizing waste, and supporting sustainable supply chains.",
    'green space preservation': "Support efforts to preserve and protect green spaces, such as parks and natural reserves, to maintain biodiversity and provide recreational areas for communities.",
    'eco-friendly transportation apps': "Use eco-friendly transportation apps to find and book sustainable travel options, such as bike-sharing, carpooling, and public transit.",
    'sustainable energy solutions': "Explore sustainable energy solutions, such as geothermal heating and cooling, to reduce reliance on fossil fuels and lower your carbon footprint.",
    'green event planning': "Plan green events by minimizing waste, using eco-friendly materials, and incorporating sustainable practices to reduce the environmental impact of gatherings.",
    'environmental education': "Promote environmental education by raising awareness about sustainability issues, supporting educational programs, and encouraging eco-friendly behaviors.",
    'ecofriendly home maintenance': "Perform eco-friendly home maintenance tasks, such as using non-toxic cleaning products and conserving water, to reduce your environmental impact.",
    'sustainable product design': "Support sustainable product design by choosing items made from environmentally friendly materials and designed for durability and minimal waste.",
    'eco friendly': "Plan green events by minimizing waste, using eco-friendly materials, and incorporating sustainable practices to reduce the environmental impact of gatherings.",
    'ecofriendly': "Plan green events by minimizing waste, using eco-friendly materials, and incorporating sustainable practices to reduce the environmental impact of gatherings.",
    'recycled content products': "Opt for products made from recycled content to reduce the demand for virgin materials and support recycling efforts.",
    'global warming':"Plan green events by minimizing waste, using eco-friendly materials, and incorporating sustainable practices to reduce the environmental impact of gatherings.",
    'ecofriendly event supplies': "Use eco-friendly event supplies, such as biodegradable tableware and reusable decorations, to minimize waste and reduce environmental impact.",
    'sustainable fashion brands': "Support sustainable fashion brands that prioritize ethical production practices, use eco-friendly materials, and reduce waste in their supply chains.",
    'clean energy initiatives': "Support clean energy initiatives and policies that promote the development and use of renewable energy sources to reduce greenhouse gas emissions.",
    'ecofriendly life': "Choose personal care products made with natural ingredients and minimal packaging. Look for certifications like 'Cruelty-Free' and 'Organic'.",
    'sustainable seafood choices': "Make sustainable seafood choices by selecting fish and shellfish that are responsibly harvested or farmed, and certified by sustainability standards."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()
        user_message = data.get('message', '').lower()

        # Find a matching response based on keywords
        response = "I'm not sure about that. Try asking about energy, recycling, or eco-friendly products."

        # Search for keywords in the user input
        for keyword in responses:
            if keyword in user_message:
                response = responses[keyword]
                break

        return jsonify({'response': response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'response': "Sorry, there was an error. Please try again."})

if __name__ == '__main__':
    app.run(debug=True)
