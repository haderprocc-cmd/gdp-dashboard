import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_tie_match():
    fig, ax = plt.subplots()
    ax.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    ax.add_patch(patches.Circle((2, 4), 0.4, color='blue'))
    ax.plot([2, 2], [3, 4], color='blue', linewidth=4)
    ax.plot([2, 1.5], [3.5, 3.2], color='blue', linewidth=3)
    ax.plot([2, 2.5], [3.5, 3.2], color='blue', linewidth=3)
    ax.plot([2, 1.7], [3, 2.5], color='blue', linewidth=3)
    ax.plot([2, 2.3], [3, 2.5], color='blue', linewidth=3)

    ax.add_patch(patches.Circle((8, 4), 0.4, color='red'))
    ax.plot([8, 8], [3, 4], color='red', linewidth=4)
    ax.plot([8, 7.5], [3.5, 3.2], color='red', linewidth=3)
    ax.plot([8, 8.5], [3.5, 3.2], color='red', linewidth=3)
    ax.plot([8, 7.7], [3, 2.5], color='red', linewidth=3)
    ax.plot([8, 8.3], [3, 2.5], color='red', linewidth=3)

    ax.add_patch(patches.Circle((5, 2.8), 0.3, edgecolor='black', facecolor='black'))

    ax.plot([4.2, 5.8], [5.2, 5.2], color='black', linewidth=3)
    ax.plot([4.2, 5.8], [4.8, 4.8], color='black', linewidth=3)

    ax.text(5, 0.5, "تعادل", fontsize=24, ha='center', fontweight='bold', color='darkgreen')

    st.pyplot(fig)

st.title("🎮 مباراة تعادل")
st.write("رسم تعبيري عن حالة تعادل بين لاعبين.")
draw_tie_match()
