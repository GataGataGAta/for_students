import streamlit as st
import plotly.graph_objects as go

# Webページのタイトル設定
st.title("凸レンズの像シミュレーター")
st.write("スライダーを動かして、光源の位置を変えてみましょう。")

# 初期設定
f = 10.0
h_obj = 5.0

# --- Streamlitのスライダー ---
a = st.slider('光源の位置(cm) [※焦点距離は10cm]', min_value=11.0, max_value=35.0, value=20.0, step=0.5)

# 計算
b = 1 / (1/f - 1/a)
mag = b / a
h_img = -h_obj * mag

# --- Plotlyでグラフを描画 ---
fig = go.Figure()

# 光軸とレンズ
fig.add_hline(y=0, line_width=1, line_color="black") # 光軸
fig.add_vline(x=0, line_width=4, line_color="blue", opacity=0.5) # レンズ

# 焦点の描画
fig.add_trace(go.Scatter(
    x=[-f, f], y=[0, 0], mode='markers+text', 
    marker=dict(color='red', size=8), 
    text=['焦点', '焦点'], textposition='bottom center', name='焦点'
))

# 光線1: 光軸に平行 -> レンズを通った後、反対側の焦点を通る
fig.add_trace(go.Scatter(
    x=[-a, 0, 35], y=[h_obj, h_obj, h_obj - (h_obj/f)*35], 
    mode='lines', line=dict(color='orange', dash='dash', width=2), name='光線'
))

# 光線2: レンズの中心を通る -> 直進する
y_end = -(h_obj/a) * 35
fig.add_trace(go.Scatter(
    x=[-a, 35], y=[h_obj, y_end], 
    mode='lines', line=dict(color='orange', dash='dash', width=2), showlegend=False
))

# 光源（実物）の矢印とテキスト
fig.add_annotation(
    x=-a, y=h_obj, ax=-a, ay=0, xref="x", yref="y", axref="x", ayref="y", 
    showarrow=True, arrowhead=2, arrowwidth=4, arrowcolor="red"
)
fig.add_annotation(x=-a, y=h_obj+1.5, text="光源", showarrow=False, font=dict(color="red", size=14))

# 像の矢印とテキスト
fig.add_annotation(
    x=b, y=h_img, ax=b, ay=0, xref="x", yref="y", axref="x", ayref="y", 
    showarrow=True, arrowhead=2, arrowwidth=4, arrowcolor="green"
)
fig.add_annotation(x=b, y=h_img-1.5, text="スクリーン(実像)", showarrow=False, font=dict(color="green", size=14))

# グラフのレイアウトとタイトルの設定
fig.update_layout(
    title=f'<b>光源の位置: {a:.1f} cm | スクリーンの位置: {b:.1f} cm | 像の大きさ(倍率): {mag:.2f}倍</b>',
    xaxis_title='位置 (cm)',
    yaxis_title='高さ (cm)',
    xaxis=dict(range=[-35, 35], showgrid=True),
    yaxis=dict(range=[-15, 15], showgrid=True),
    height=500,
    showlegend=False
)

# Streamlit上にグラフを表示
st.plotly_chart(fig, use_container_width=True)