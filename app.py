from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_code = '''
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Çoktan Seçmeli Soru</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }
            .quiz-container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
                box-sizing: border-box;
            }
            .question-container {
                margin-bottom: 20px;
                display: none;
            }
            .question-title {
                font-size: 18px;
                margin-bottom: 10px;
            }
            .options {
                list-style-type: none;
                padding: 0;
            }
            .options li {
                margin-bottom: 8px;
            }
            .submit-button, .next-button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                margin-top: 10px;
            }
            .submit-button:hover, .next-button:hover {
                background-color: #45a049;
            }
            #result {
                margin-top: 20px;
                font-size: 18px;
            }
            #maxScore {
                position: absolute;
                top: 20px;
                right: 20px;
                font-size: 18px;
            }
            footer {
                position: absolute;
                bottom: 20px;
                width: 100%;
                text-align: center;
                font-size: 14px;
                color: #666;
            }
        </style>
    </head>
    <body>

    <div id="maxScore">En Yüksek Puan: 0</div>

    <div class="quiz-container" id="quiz">
        <div class="question-container" id="question1">
            <div class="question-title">Python'da yapay zeka (AI) modelleri geliştirmek için hangi kütüphane yaygın olarak kullanılır?</div>
            <form>
                <ul class="options">
                    <li><label><input type="radio" name="q1" value="NumPy"> NumPy</label></li>
                    <li><label><input type="radio" name="q1" value="Pandas"> Pandas</label></li>
                    <li><label><input type="radio" name="q1" value="TensorFlow"> TensorFlow</label></li>
                    <li><label><input type="radio" name="q1" value="Matplotlib"> Matplotlib</label></li>
                </ul>
            </form>
        </div>

        <div class="question-container" id="question2">
            <div class="question-title">Bilgisayar görüşü (Computer Vision) uygulamalarında hangi algoritma genellikle nesne tanıma için kullanılır?</div>
            <form>
                <ul class="options">
                    <li><label><input type="radio" name="q2" value="K-means"> K-ortalama (K-means)</label></li>
                    <li><label><input type="radio" name="q2" value="Decision Trees"> Karar Ağaçları</label></li>
                    <li><label><input type="radio" name="q2" value="CNN"> Konvolüsyonel Sinir Ağları (CNN)</label></li>
                    <li><label><input type="radio" name="q2" value="SVM"> Destek Vektör Makineleri (SVM)</label></li>
                </ul>
            </form>
        </div>

        <div class="question-container" id="question3">
            <div class="question-title">Doğal dil işleme (NLP) görevlerinde, hangi model genellikle dil modelleme ve metin üretimi için kullanılır?</div>
            <form>
                <ul class="options">
                    <li><label><input type="radio" name="q3" value="LSTM"> LSTM</label></li>
                    <li><label><input type="radio" name="q3" value="GAN"> GAN</label></li>
                    <li><label><input type="radio" name="q3" value="KNN"> KNN</label></li>
                    <li><label><input type="radio" name="q3" value="RNN"> RNN</label></li>
                </ul>
            </form>
        </div>

        <div class="question-container" id="question4">
            <div class="question-title">Python'da bir yapay zeka modelini eğitmek için hangi fonksiyon kullanılır?</div>
            <form>
                <ul class="options">
                    <li><label><input type="radio" name="q4" value="fit"> fit()</label></li>
                    <li><label><input type="radio" name="q4" value="predict"> predict()</label></li>
                    <li><label><input type="radio" name="q4" value="transform"> transform()</label></li>
                    <li><label><input type="radio" name="q4" value="compile"> compile()</label></li>
                </ul>
            </form>
        </div>

        <button id="nextButton" class="next-button" onclick="nextQuestion()">Diğer soruya geç</button>
        <button id="submitButton" class="submit-button" onclick="checkAnswers()" style="display:none;">Gönder</button>
        <div id="result"></div>
    </div>

    <footer>
        Geliştirici: [SUDE ESMER]
    </footer>

    <script>
        const correctAnswers = {
            q1: "TensorFlow",
            q2: "CNN",
            q3: "LSTM",
            q4: "fit"
        };

        let currentQuestionIndex = 0;
        let highestScore = 0;
        let score = 0;

        function showQuestion(index) {
            const questions = document.querySelectorAll('.question-container');
            questions.forEach((question, i) => {
                question.style.display = i === index ? 'block' : 'none';
            });
        }

        function nextQuestion() {
            const currentQuestion = document.querySelector(`#question${currentQuestionIndex + 1}`);
            const selectedAnswer = currentQuestion.querySelector('input:checked');

            if (selectedAnswer) {
                if (selectedAnswer.value === correctAnswers[`q${currentQuestionIndex + 1}`]) {
                    score += 25;
                }
                currentQuestionIndex++;
                if (currentQuestionIndex < 4) {
                    showQuestion(currentQuestionIndex);
                } else {
                    document.getElementById('nextButton').style.display = 'none';
                    document.getElementById('submitButton').style.display = 'block';
                }
            } else {
                alert('Lütfen bir cevap seçiniz!');
            }
        }

        function checkAnswers() {
            document.getElementById('result').textContent = `Toplam Puan: ${score}`;
            document.getElementById('result').style.color = score > 0 ? "green" : "red";

            if (score > highestScore) {
                highestScore = score;
                document.getElementById('maxScore').textContent = `En Yüksek Puan: ${highestScore}`;
            }
        }

        showQuestion(currentQuestionIndex);
    </script>

    </body>
    </html>
    '''
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)




