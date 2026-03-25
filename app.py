import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib  # グラフの日本語表示用

# Webページのタイトル設定
st.title("凸レンズの像シミュレーター")
st.write("スライダーを動かして、光源の位置を変えてみましょう。")

# 初期設定
f = 10.0
h_obj = 5.0

# --- Streamlitのスライダー ---
# ユーザーがWeb上で操作できるスライダーを配置
a = st.slider('光源の位置(cm) [※焦点距離は10cm]', min_value=11.0, max_value=35.0, value=20.0, step=0.5)

# --- グラフの描画 ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-35, 35)
ax.set_ylim(-15, 15)

ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='blue', lw=3, alpha=0.5, label='凸レンズ')
ax.plot([-f, f], [0, 0], 'ro', markersize=6, label='焦点')

# 計算
b = 1 / (1/f - 1/a)
mag = b / a

# 光源と像の描画
ax.annotate('', xy=(-a, h_obj), xytext=(-a, 0), arrowprops=dict(facecolor='red', width=3, headwidth=10))
ax.text(-a, h_obj + 1, '光源', ha='center', color='red')

h_img = -h_obj * mag
ax.annotate('', xy=(b, h_img), xytext=(b, 0), arrowprops=dict(facecolor='green', width=3, headwidth=10))
ax.text(b, h_img - 2, 'スクリーン(実像)', ha='center', color='green')

# 光線の作図
ax.plot([-a, 0, 35], [h_obj, h_obj, h_obj - (h_obj/f)*35], 'orange', linestyle='--', alpha=0.8)
y_end = -(h_obj/a) * 35
ax.plot([-a, 35], [h_obj, y_end], 'orange', linestyle='--', alpha=0.8)

ax.set_title(f'光源の位置: {a:.1f} cm | スクリーンの位置: {b:.1f} cm | 像の大きさ(倍率): {mag:.2f}倍')
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.6)

# --- Streamlit上にグラフを表示 ---
st.pyplot(fig)