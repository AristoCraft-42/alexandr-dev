"""Builds the nails/ and massage/ demos from barber/index.html (same booking flow, other theme and texts).

Run after changing the barber demo: python make_variants.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, 'barber', 'index.html'), encoding='utf-8').read()

COMMON_FROM = {
    'h1,h2,h3 { font-family:Oswald, Impact, sans-serif; letter-spacing:.5px; text-transform:uppercase; margin:0; }':
        'h1,h2,h3 { font-family:"{HFONT}", Georgia, serif; letter-spacing:0; margin:0; font-weight:600; }',
    '.logo { font-family:Oswald, sans-serif;': '.logo { font-family:"{HFONT}", serif;',
    'font-family:Oswald, sans-serif; font-size:26px;': 'font-family:"{HFONT}", serif; font-size:26px;',
}

VARIANTS = {
    'nails': {
        'HFONT': 'Playfair Display',
        'fonts': 'family=Playfair+Display:wght@500;600&family=Inter:wght@400;600',
        'vars': ':root { --bg:#fbf6f4; --card:#ffffff; --line:#eddcd6; --text:#3a2a2c; --muted:#8f7a7c; --gold:#c9727f; --r:14px; }',
        'repl': {
            '<title>Барбершоп «Ферзь» — демо</title>': '<title>Студия маникюра «Миндаль» — демо</title>',
            'барбершоп вымышленный': 'студия вымышленная',
            '<div class="logo">Ф<b>Е</b>РЗЬ</div>': '<div class="logo">Минд<b>а</b>ль</div>',
            '📍 ул. Садовая, 12': '📍 ул. Лесная, 7',
            'Стрижка, после которой <span>хочется вернуться</span>': 'Маникюр, который <span>держится три недели</span>',
            'Мужские стрижки, бритьё и уход за бородой. Без очередей: запись онлайн за 30 секунд.':
                'Маникюр, педикюр и наращивание. Стерильные инструменты, запись онлайн за 30 секунд.',
            '<b>4.9 ★</b>412 отзывов': '<b>4.9 ★</b>238 отзывов',
            '<b>с 10 до 22</b>без выходных': '<b>с 9 до 21</b>без выходных',
            '<b>5 мин</b>от метро': '<b>3 мин</b>от метро',
            'Записался через сайт ночью, утром уже стригся. Артём — топ, наконец-то нормальный фейд.':
                'Записалась через сайт за минуту, без звонков. Покрытие у Алины держится уже третью неделю.',
            'Игорь · 2ГИС': 'Ольга · 2ГИС',
            'Удобно, что напоминание приходит накануне. Ни разу не забыл.':
                'Нравится, что видно свободные окна и напоминание приходит накануне.',
            'Максим · Яндекс Карты': 'Марина · Яндекс Карты',
            'ул. Садовая, 12, вход со двора': 'ул. Лесная, 7, 2 этаж',
            'ежедневно 10:00–22:00': 'ежедневно 9:00–21:00',
            'Барбершоп «Ферзь» — демо.': 'Студия маникюра «Миндаль» — демо.',
            "color:#141210": "color:#fff",
            'background:#1a1714;': 'background:#fff8f6;',
            '.day.sel { border-color:var(--gold); background:#2a2318; }': '.day.sel { border-color:var(--gold); background:#f8e4e7; }',
            'linear-gradient(180deg, rgba(20,18,16,.2), var(--bg)),\n      repeating-linear-gradient(135deg, #1b1815 0 18px, #181512 18px 36px)':
                'radial-gradient(circle at 85% 20%, #f3d3d8 0 160px, transparent 161px),\n      linear-gradient(180deg, #f9ebe8, var(--bg))',
            'repeating-linear-gradient(0deg, #1b1815 0 29px, #24201b 29px 30px), repeating-linear-gradient(90deg, transparent 0 29px, #24201b 29px 30px); background-blend-mode: lighten;':
                'repeating-linear-gradient(0deg, #fff 0 29px, #f1e4e0 29px 30px), repeating-linear-gradient(90deg, transparent 0 29px, #f1e4e0 29px 30px); background-blend-mode: darken;',
            '.sheet-bg { position:fixed; inset:0; background:rgba(0,0,0,.6);': '.sheet-bg { position:fixed; inset:0; background:rgba(58,42,44,.45);',
        },
        'services': """const SERVICES = [
  { id: 'mani', name: 'Маникюр без покрытия', dur: 60, price: 1200 },
  { id: 'gel', name: 'Маникюр + гель-лак', dur: 90, price: 2200 },
  { id: 'ext', name: 'Наращивание', dur: 150, price: 3500 },
  { id: 'pedi', name: 'Педикюр + гель-лак', dur: 90, price: 2600 },
  { id: 'design', name: 'Дизайн (2 ногтя)', dur: 15, price: 300 },
  { id: 'remove', name: 'Снятие покрытия', dur: 20, price: 400 },
];
const MASTERS = [
  { id: 'any', name: 'Любой мастер', role: 'ближайшее время', color: '#c9b2b5' },
  { id: 'alina', name: 'Алина', role: 'топ-мастер · 7 лет', color: '#c9727f' },
  { id: 'vika', name: 'Виктория', role: 'мастер · 4 года', color: '#d9a07a' },
  { id: 'dasha', name: 'Дарья', role: 'мастер педикюра · 5 лет', color: '#a78bb0' },
];""",
        'done_master': "'Мастер: Виктория'",
    },
    'massage': {
        'HFONT': 'Lora',
        'fonts': 'family=Lora:wght@500;600&family=Inter:wght@400;600',
        'vars': ':root { --bg:#f3f1ea; --card:#fffdf7; --line:#ddd8c8; --text:#2d3a2e; --muted:#76806f; --gold:#5f7d5a; --r:14px; }',
        'repl': {
            '<title>Барбершоп «Ферзь» — демо</title>': '<title>Массажный кабинет «Тепло» — демо</title>',
            'барбершоп вымышленный': 'кабинет вымышленный',
            '<div class="logo">Ф<b>Е</b>РЗЬ</div>': '<div class="logo">Тепл<b>о</b></div>',
            '📍 ул. Садовая, 12': '📍 пр. Мира, 40',
            'Стрижка, после которой <span>хочется вернуться</span>': 'Массаж, после которого <span>отпускает спина</span>',
            'Мужские стрижки, бритьё и уход за бородой. Без очередей: запись онлайн за 30 секунд.':
                'Классический, спортивный и расслабляющий массаж. Свободные окна видны сразу, запись за 30 секунд.',
            '<b>4.9 ★</b>412 отзывов': '<b>5.0 ★</b>127 отзывов',
            '<b>с 10 до 22</b>без выходных': '<b>с 9 до 21</b>пн–сб',
            '<b>5 мин</b>от метро': '<b>парковка</b>у входа',
            'Записался через сайт ночью, утром уже стригся. Артём — топ, наконец-то нормальный фейд.':
                'Записался вечером на утро, без звонков. После трёх сеансов у Сергея шея наконец не болит.',
            'Игорь · 2ГИС': 'Андрей · 2ГИС',
            'Удобно, что напоминание приходит накануне. Ни разу не забыл.':
                'Удобно выбирать время самой, а накануне приходит напоминание.',
            'Максим · Яндекс Карты': 'Елена · Яндекс Карты',
            'ул. Садовая, 12, вход со двора': 'пр. Мира, 40, офис 3',
            'ежедневно 10:00–22:00': 'пн–сб 9:00–21:00',
            'Барбершоп «Ферзь» — демо.': 'Массажный кабинет «Тепло» — демо.',
            "color:#141210": "color:#fff",
            'background:#1a1714;': 'background:#faf8f2;',
            '.day.sel { border-color:var(--gold); background:#2a2318; }': '.day.sel { border-color:var(--gold); background:#e3ebdf; }',
            'linear-gradient(180deg, rgba(20,18,16,.2), var(--bg)),\n      repeating-linear-gradient(135deg, #1b1815 0 18px, #181512 18px 36px)':
                'radial-gradient(circle at 90% 30%, #dfe7d6 0 180px, transparent 181px),\n      linear-gradient(180deg, #e9eee0, var(--bg))',
            'repeating-linear-gradient(0deg, #1b1815 0 29px, #24201b 29px 30px), repeating-linear-gradient(90deg, transparent 0 29px, #24201b 29px 30px); background-blend-mode: lighten;':
                'repeating-linear-gradient(0deg, #fffdf7 0 29px, #e6e1d2 29px 30px), repeating-linear-gradient(90deg, transparent 0 29px, #e6e1d2 29px 30px); background-blend-mode: darken;',
            '.sheet-bg { position:fixed; inset:0; background:rgba(0,0,0,.6);': '.sheet-bg { position:fixed; inset:0; background:rgba(45,58,46,.45);',
        },
        'services': """const SERVICES = [
  { id: 'classic', name: 'Классический массаж спины', dur: 40, price: 1800 },
  { id: 'full', name: 'Общий массаж', dur: 90, price: 3500 },
  { id: 'neck', name: 'Шейно-воротниковая зона', dur: 30, price: 1400 },
  { id: 'sport', name: 'Спортивный массаж', dur: 60, price: 2800 },
  { id: 'relax', name: 'Расслабляющий с маслами', dur: 60, price: 2600 },
  { id: 'lymph', name: 'Лимфодренажный', dur: 60, price: 2900 },
];
const MASTERS = [
  { id: 'any', name: 'Любой специалист', role: 'ближайшее время', color: '#a8b09c' },
  { id: 'sergey', name: 'Сергей', role: 'массажист · 10 лет', color: '#5f7d5a' },
  { id: 'anna', name: 'Анна', role: 'массажист · 6 лет', color: '#b08a5f' },
];""",
        'done_master': "'Специалист: Анна'",
    },
}


def build(name, v):
    t = SRC
    for a, b in COMMON_FROM.items():
        assert a in t, a
        t = t.replace(a, b.replace('{HFONT}', v['HFONT']))
    t = t.replace('family=Oswald:wght@500;700&family=Inter:wght@400;600', v['fonts'])
    t = t.replace(':root { --bg:#141210; --card:#1e1b18; --line:#332e28; --text:#f3ede4; --muted:#a89d8e; --gold:#d4a24c; --r:14px; }', v['vars'])
    for a, b in v['repl'].items():
        assert a in t, a
        t = t.replace(a, b)
    i, j = t.index('const SERVICES = ['), t.index('const rub =')
    t = t[:i] + v['services'] + '\n' + t[j:]
    t = t.replace("m.name === 'Любой мастер' ? 'Мастер: Денис'", f"m.id === 'any' ? {v['done_master']}")
    t = t.replace("'Мастер: ' + m.name", "'Мастер: ' + m.name" if name == 'nails' else "'Специалист: ' + m.name")
    os.makedirs(os.path.join(HERE, name), exist_ok=True)
    open(os.path.join(HERE, name, 'index.html'), 'w', encoding='utf-8', newline='\n').write(t)


for n, v in VARIANTS.items():
    build(n, v)
    print('built', n)
