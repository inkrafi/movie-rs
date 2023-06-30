import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Website Rekomendasi Film",
    page_icon="🎥",
)

st.title("Sistem Rekomendasi Film")
# st.sidebar.success("Select a page above")

image = Image.open('assets/img/Cinema.jpg')
st.image(image)  # caption='Image by macrovector on Freepik'

st.markdown('Selamat datang di website rekomendasi film! Di sini, Anda dapat menemukan berbagai rekomendasi film yang menarik dan sesuai dengan preferensi Anda. Kami menggunakan metode content-based filtering untuk memberikan rekomendasi yang didasarkan pada kesamaan konten seperti genre, aktor, dan sinopsis film. Meskipun database kami memiliki lebih dari 600.000 film, perlu diketahui bahwa saat ini belum terdapat film-film Indonesia dalam koleksi kami.')
st.markdown('Namun, jangan khawatir! Sistem kami tetap memberikan rekomendasi film yang berkualitas dan bervariasi dari berbagai genre dan negara lainnya. Kami berharap Anda dapat menemukan film-film baru yang menarik dan menghibur melalui pengalaman menggunakan website ini. Selamat menikmati menonton film-film pilihan Anda dan semoga rekomendasi kami dapat memenuhi harapan dan kepuasan Anda sebagai penikmat film. Terima kasih telah mengunjungi website kami!')


# Button
def redirect_button(url: str, text: str = None, color="#1E4070"):
    st.markdown(
        f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 5px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
        unsafe_allow_html=True
    )


redirect_button("/Rekomendasi", "Cari Rekomendasi Film")
