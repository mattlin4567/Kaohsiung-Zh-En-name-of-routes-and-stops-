高雄市公車中英文路線與站牌資料
===================

雖然政府在開放資料上的進步有目共睹，但還是需要不斷的完善更新，雖然可以從高雄市政府或交通部的開放資料平台取得路線與站牌的資料，卻缺乏英文的部分，因此開發一個小程式，從公車動態資訊網站將英文站牌與路線抓取並輸出成需要的格式。

資料來源為[高雄市公車動態資訊](http://122.146.229.210/bus/Default.aspx)，透過 [Tamper](https://chrome.google.com/webstore/detail/tamper-chrome-extension/hifhgpdkfodlpnlmlnmhchnkepplebkb) 取得 API ，再利用 Python 開發，將資料輸出成 JSON 格式。

----------

用法
-------------
Python 3+ 的環境下，執行以下指令

    $ python crawler.py

執行成功後會在該目錄產生 **kaohsiung_stopOfRoute.json** 檔案

輸出格式
-------------

    kaohsiung_stopOfRoute.json{     
	    id(string): 路線識別代碼,
        routeName(NameType): 路線名稱,
        goRoute(stops): 去程所有經過站牌,
        backRoute(stops): 返程所有經過站牌
    }
    NameType{
        en(string): 中文繁體名稱,
        zh(string): 英文名稱
    }
    stops{ 	
	    sequence(string): 路線經過站牌之順序,
        en(string): 中文繁體名稱,
        zh(string): 英文名稱  
    }
關於
-------------
我只有用單執行緒去將資料接回來後再處理並輸出，所以執行時間大概是5分鐘左右，所以歡迎大家 fork 或直接 contribute。

Licience
-------------
MIT
