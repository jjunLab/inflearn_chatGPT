import streamlit as st
import pandas as pd

st.title('데이터프레임 튜토리얼')

# DataFrame 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
st.dataframe(dataframe, use_container_width=False)


# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(dataframe)


# # 메트릭
st.metric(label="온도", value="10°C", delta="1.2°C")
st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

# Json
gpt_response = {
  "id": "chatcmpl-7YTjS8XYFfX6qECRIhO5dEN6piHV9",
  "object": "chat.completion",
  "created": 1688451798,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "To make a pizza, you will need the following ingredients and equipment:\n\nIngredients:\n- Pizza dough\n- Pizza sauce\n- Cheese (mozzarella is commonly used, but you can use any type you like)\n- Toppings (such as pepperoni, bell peppers, onions, mushrooms, olives, etc.)\n- Olive oil\n- Salt and pepper (optional)\n\nEquipment:\n- Baking sheet or pizza stone\n- Rolling pin (if your dough needs to be rolled out)\n- Oven\n\nHere's a step-by-step guide to making a pizza:\n\n1. Preheat the oven: Preheat your oven to the recommended temperature mentioned on your pizza dough packaging (usually around 475\u00b0F/245\u00b0C) and allow it to fully heat up.\n\n2. Prepare the dough: If you are using store-bought dough, follow the package instructions for any necessary preparation. If you prefer to make your own dough, there are many recipes available online to guide you through the process.\n\n3. Roll out the dough: On a clean, lightly floured surface, roll out the dough with a rolling pin to your desired thickness. Aim for a round or rectangular shape, depending on your preference.\n\n4. Prepare the baking surface: Sprinkle some flour or use parchment paper on a baking sheet or pizza stone to prevent sticking.\n\n5. Transfer the dough: Once the dough is rolled out, transfer it to the baking sheet or pizza stone. Gently stretch it to fit the shape if necessary.\n\n6. Add the sauce: Spoon pizza sauce onto the dough and spread it evenly with the back of a spoon. Leave a small border at the edges for the crust.\n\n7. Add cheese and toppings: Sprinkle shredded cheese generously over the sauce, covering the entire pizza. Next, add your preferred toppings, distributing them evenly across the pizza.\n\n8. Optional: Seasoning: If you like, you can sprinkle a bit of salt and pepper on top of the cheese and toppings for added flavor.\n\n9. Bake the pizza: Carefully place the pizza in the preheated oven. The baking time will vary based on your oven and the thickness of your pizza but usually falls between 10-15 minutes. Keep an eye on it to avoid burning.\n\n10. Cool and serve: Once the cheese is melted and the crust is golden brown, remove the pizza from the oven. Allow it to cool for a few minutes before slicing and serving.\n\nRemember, these steps act as a general guide, and you can customize your pizza with your preferred ingredients, seasonings, and cooking techniques as you like. Have fun and enjoy your homemade pizza!"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 529,
    "total_tokens": 543
  }
}
st.json(gpt_response)

