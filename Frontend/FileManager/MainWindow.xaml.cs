using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace FileManager
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private bool flagAllTru = false;
        private bool flagTypTru = false;

        public MainWindow()
        {
            InitializeComponent();

            //getValueRadioButton
            radioButton1.IsChecked = Properties.Settings.Default.radioButton1;
            radioButton2.IsChecked = Properties.Settings.Default.radioButton2;

            //getValueAdditionalOption
             checkBox1.IsChecked = Properties.Settings.Default.Sort;
             checkBox2.IsChecked = Properties.Settings.Default.Move;

            //getValueAllTrue
            AllTrue1.IsChecked = Properties.Settings.Default.AllTrue1;
            AllTrue2.IsChecked = Properties.Settings.Default.AllTrue2;
            AllTrue3.IsChecked = Properties.Settings.Default.AllTrue3;
            AllTrue4.IsChecked = Properties.Settings.Default.AllTrue4;
            AllTrue5.IsChecked = Properties.Settings.Default.AllTrue5;
            AllTrue6.IsChecked = Properties.Settings.Default.AllTrue6;
            AllTrue7.IsChecked = Properties.Settings.Default.AllTrue7;

            //getValueAudioCheckBox
            aif.IsChecked = Properties.Settings.Default.aif;
            cda.IsChecked = Properties.Settings.Default.cda;
            mid.IsChecked = Properties.Settings.Default.mid;
            midi.IsChecked = Properties.Settings.Default.midi;
            mp3.IsChecked = Properties.Settings.Default.mp3;
            mpa.IsChecked = Properties.Settings.Default.mpa;
            ogg.IsChecked = Properties.Settings.Default.ogg;
            wav.IsChecked = Properties.Settings.Default.wav;
            wma.IsChecked = Properties.Settings.Default.wma;
            wpl.IsChecked = Properties.Settings.Default.wpl;

            //getValueVideoCheckBox
            three_g2.IsChecked = Properties.Settings.Default.three_g2;
            three_gp.IsChecked = Properties.Settings.Default.three_gp;
            avi.IsChecked = Properties.Settings.Default.avi;
            flv.IsChecked = Properties.Settings.Default.flv;
            h264.IsChecked = Properties.Settings.Default.h264;
            m4v.IsChecked = Properties.Settings.Default.m4v;
            mkv.IsChecked = Properties.Settings.Default.mkv;
            mov.IsChecked = Properties.Settings.Default.mov;
            mp4.IsChecked = Properties.Settings.Default.mp4;
            mpg.IsChecked = Properties.Settings.Default.mpg;
            mpeg.IsChecked = Properties.Settings.Default.mpeg;
            rm.IsChecked = Properties.Settings.Default.rm;
            swf.IsChecked = Properties.Settings.Default.swf;
            vob.IsChecked = Properties.Settings.Default.vob;
            vmv.IsChecked = Properties.Settings.Default.wmv;

            //getValueArchiveCheckBox
            seven_z.IsChecked = Properties.Settings.Default.Seven_z;
            arj.IsChecked = Properties.Settings.Default.arj;
            deb.IsChecked = Properties.Settings.Default.deb;
            pkg.IsChecked = Properties.Settings.Default.pkg;
            rar.IsChecked = Properties.Settings.Default.rar;
            rpm.IsChecked = Properties.Settings.Default.rpm;
            tar_gz.IsChecked = Properties.Settings.Default.tar_gz;
            z.IsChecked = Properties.Settings.Default.z;
            zip.IsChecked = Properties.Settings.Default.zip;

            //getValueTableCheckBox
            ods.IsChecked = Properties.Settings.Default.ods;
            xlr.IsChecked = Properties.Settings.Default.xlr;
            xls.IsChecked = Properties.Settings.Default.xls;
            xlsx.IsChecked = Properties.Settings.Default.xlsx;
            csv.IsChecked = Properties.Settings.Default.csv;

            //getValueDocumentCheckBox
            doc.IsChecked = Properties.Settings.Default.doc;
            docx.IsChecked = Properties.Settings.Default.docx;
            odt.IsChecked = Properties.Settings.Default.odt;
            pdf.IsChecked = Properties.Settings.Default.pdf;
            rtf.IsChecked = Properties.Settings.Default.rtf;
            tex.IsChecked = Properties.Settings.Default.tex;
            txt.IsChecked = Properties.Settings.Default.txt;
            wks.IsChecked = Properties.Settings.Default.wks;
            wps.IsChecked = Properties.Settings.Default.wps;
            wpd.IsChecked = Properties.Settings.Default.wpd;

            //getValuePresentationCheckBox
            key.IsChecked = Properties.Settings.Default.key;
            odp.IsChecked = Properties.Settings.Default.odp;
            pps.IsChecked = Properties.Settings.Default.pps;
            ppt.IsChecked = Properties.Settings.Default.ppt;
            pptx.IsChecked = Properties.Settings.Default.pptx;

            //getValueImageCheckBox
            ai.IsChecked = Properties.Settings.Default.ai;
            bmp.IsChecked = Properties.Settings.Default.bmp;
            gif.IsChecked = Properties.Settings.Default.gif;
            ico.IsChecked = Properties.Settings.Default.ico;
            jpeg.IsChecked = Properties.Settings.Default.jpeg;
            jpg.IsChecked = Properties.Settings.Default.jpg;
            png.IsChecked = Properties.Settings.Default.png;
            ps.IsChecked = Properties.Settings.Default.ps;
            psd.IsChecked = Properties.Settings.Default.psd;
            svg.IsChecked = Properties.Settings.Default.svg;
            tif.IsChecked = Properties.Settings.Default.tif;
            tiff.IsChecked = Properties.Settings.Default.tiff;
        }

        private void OK_Click(object sender, RoutedEventArgs e)
        {
            //radioButton
            Properties.Settings.Default.radioButton1 = radioButton1.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.radioButton2 = radioButton2.IsChecked.GetValueOrDefault();

            //AdditionalOptions
            Properties.Settings.Default.Sort = checkBox1.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.Move = checkBox2.IsChecked.GetValueOrDefault();

            //AllTrueCheckBox
            Properties.Settings.Default.AllTrue1 = AllTrue1.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.AllTrue2 = AllTrue2.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.AllTrue3 = AllTrue3.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.AllTrue4 = AllTrue4.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.AllTrue5 = AllTrue5.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.AllTrue6 = AllTrue6.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.AllTrue7 = AllTrue7.IsChecked.GetValueOrDefault();

            //AudioCheckBox
            Properties.Settings.Default.aif = aif.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.cda = cda.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mid = mid.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.midi = midi.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mp3 = mp3.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mpa = mpa.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.ogg = ogg.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.wav = wav.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.wma = wma.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.wpl = wpl.IsChecked.GetValueOrDefault();

            //VideoCheckBox
            Properties.Settings.Default.three_g2 = three_g2.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.three_gp = three_gp.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.avi = avi.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.flv = flv.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.h264 = h264.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.m4v = m4v.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mkv = mkv.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mov = mov.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mp4 = mp4.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mpg = mpg.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.mpeg = mpeg.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.rm = rm.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.swf = swf.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.vob = vob.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.wmv = vmv.IsChecked.GetValueOrDefault();

            //ArchiveCheckBox
            Properties.Settings.Default.Seven_z = seven_z.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.arj = arj.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.deb = deb.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.pkg = pkg.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.rar = rar.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.rpm = rpm.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.tar_gz = tar_gz.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.z = z.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.zip = zip.IsChecked.GetValueOrDefault();

            //TableCheckBox
            Properties.Settings.Default.ods = ods.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.xlr = xlr.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.xls = xls.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.xlsx = xlsx.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.csv = csv.IsChecked.GetValueOrDefault();

            //DocumentCheckBox
            Properties.Settings.Default.doc = doc.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.docx = docx.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.odt = odt.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.pdf = pdf.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.rtf = rtf.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.tex = tex.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.txt = txt.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.wks = wks.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.wps = wps.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.wpd = wpd.IsChecked.GetValueOrDefault();

            //PresentationCheckBox
            Properties.Settings.Default.key = key.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.odp = odp.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.pps = pps.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.ppt = ppt.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.pptx = pptx.IsChecked.GetValueOrDefault();

            //ImageCheckBox
            Properties.Settings.Default.ai = ai.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.bmp = bmp.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.gif = gif.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.ico = ico.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.jpeg = jpeg.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.jpg = jpg.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.png = png.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.ps = ps.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.psd = psd.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.svg = svg.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.tif = tif.IsChecked.GetValueOrDefault();
            Properties.Settings.Default.tiff = tiff.IsChecked.GetValueOrDefault();

            //SaveSettings
            Properties.Settings.Default.Save();

            Application.Current.Shutdown();
        }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
        
        private void AllTrue_Checked(object sender, RoutedEventArgs e)
        {
            CheckBox ch = (CheckBox)sender;
            string c = ch.Name;
            Grid grid = (Grid)((CheckBox)this.FindName(c)).Parent;
            foreach (UIElement el in grid.Children)
            {
                if (el is ListBox)
                {
                    foreach (CheckBox item in ((ListBox)el).Items)
                    {
                        item.IsChecked = true;
                    }
                }
            }
        }

        private void AllTrue_Unchecked(object sender, RoutedEventArgs e)
        {
            CheckBox ch = (CheckBox)sender;
            string c = ch.Name;
            Grid grid = (Grid)((CheckBox)this.FindName(c)).Parent;
            foreach (UIElement el in grid.Children)
            {
                if (el is ListBox)
                {
                    foreach (CheckBox item in ((ListBox)el).Items)
                    {
                        item.IsChecked = false;
                    }
                }
            }
        }

        private void SelectAll_Indeterminate(object sender, RoutedEventArgs e)
        {
            int numCheked = 0;
            CheckBox ch = (CheckBox)sender;
            string c = ch.Name;
            Grid grid = (Grid)((CheckBox)this.FindName(c)).Parent;
            ListBox? list = null;
            foreach (UIElement el in grid.Children)
            {
                if (el is ListBox)
                {
                    list = (ListBox)el;
                    foreach (CheckBox item in list.Items)
                    {
                        if (item.IsChecked == true) numCheked++;
                    }
                }
            }

            if (numCheked == list.Items.Count)
            {
                ch.IsChecked = false;
            }
        }

        private void SetCheckedState(object sender)
        {
            int numCheked = 0;
            CheckBox ch = (CheckBox)sender;
            string c = ch.Name;
            ListBox list = (ListBox)(ch).Parent;
            CheckBox? allCheckBox = null;
            foreach (UIElement el in ((Grid)(list.Parent)).Children)
            {
                if (el is CheckBox) allCheckBox = (CheckBox)el;
            }
            foreach (CheckBox item in list.Items)
            {
                if (item.IsChecked == true) numCheked++;
            }

            if (numCheked == list.Items.Count)
            {
                allCheckBox.IsChecked = true;
            }
            else if (numCheked == 0)
            {
                allCheckBox.IsChecked = false;
            }
            else
            {
                allCheckBox.IsChecked = null;
            }
        }

        private void Option_Checked(object sender, RoutedEventArgs e)
        {
            SetCheckedState(sender);
        }

        private void Option_Unchecked(object sender, RoutedEventArgs e)
        {
            SetCheckedState(sender);
        }
    }
}
