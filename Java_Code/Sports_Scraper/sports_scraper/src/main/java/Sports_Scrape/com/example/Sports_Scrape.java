package Sports_Scrape.com.example;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URI;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

//javac -classpath jsoup-1.17.2.jar;. Sports_Scrape.java
//java -cp jsoup-1.17.2.jar Sports_Scrape.java
public class Sports_Scrape {

    private String href;
    private String data_text;
    private String name;
    private String price;
    private URL obj;
    private HttpURLConnection connection;
    private int responseCode;
    private BufferedReader input;
    private String inputLine;
    private StringBuilder response;

    // @Override
    // public String toString() {
    // return "{ \"href\":\"" + href + "\", "
    // + " \"name\": \"" + name + "\"}";
    // }

    public String getHref() {
        return href;
    }

    public void setHref(String newHref) {
        this.href = newHref;
    }

    public String setup_connection() {
        String nba_url = "https://www.espn.com/nba/schedule";
        // optional request header
        try {
            obj = new URI(nba_url).toURL();
            connection = (HttpURLConnection) obj.openConnection();
            connection.setRequestProperty("User-Agent", "Mozilla/5.0");
            responseCode = connection.getResponseCode();
            System.out.println("Response code: " + responseCode);
            input = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            response = new StringBuilder();

            while ((inputLine = input.readLine()) != null) {
                response.append(inputLine);
            }

            input.close();
            String html = response.toString();
            return html;
        } catch (Exception e) {
            System.out.println(e);
        }
        return "";
    }

    public List<ArrayList<String>> parse_html(String html) {
        Document doc = Jsoup.parse(html);
        Elements game_info = doc.select("div.Table__Title, a[data-track-linkid=\"nba:schedule:team\"]");

        List<ArrayList<String>> games = new ArrayList<ArrayList<String>>();
        List<String> days = Arrays.asList("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");

        int i = -1;
        for (Element game : game_info) {
            String info = game.text();
            String[] info_ray = info.split(",");
            if (days.contains(info_ray[0])) {
                ArrayList<String> newGameDay = new ArrayList<String>();
                games.add(newGameDay);
                i++;
            }
            if ((!info.equals(",")) && (!info.equals(""))) {
                games.get(i).add(info);
            }
        }

        System.out.println(games);
        return games;
    }

    public void odds_and_news(List<ArrayList<String>> weeks_games) {

    }

    public static void main(String[] args) {
        Sports_Scrape parser = new Sports_Scrape();
        String html = parser.setup_connection();
        List<ArrayList<String>> weeks_games = parser.parse_html(html);
        parser.odds_and_news(weeks_games);
    }
}